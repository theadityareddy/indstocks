import json
import re
import requests
from bs4 import BeautifulSoup


class Screener:
    def __init__(self, ticker):
        # print("Invoked Screener Module")
        self.ticker = ticker

    def get_soup(self):
        self.screener_URL = (
            "https://www.screener.in/company/" + self.ticker + "/consolidated"
        )
        api_response = requests.get(self.screener_URL).text
        
        self.soup = BeautifulSoup(api_response, "html.parser")

    def stock_information(self):
        """
        Retrieves stock information from the self.soup object and returns a dictionary containing the following information:

        Parameters:
        - self: The instance of the class.

        Returns:
        - stock_info: A dictionary containing the following keys:
            - name: The name of the stock.
            - about: A brief description of the stock.
            - link: The link to the stock's website.
            - bse_link: The link to the stock's BSE page.
            - nse_link: The link to the stock's NSE page (empty string if not available).
            - sector: The sector the stock belongs to.
            - industry: The industry the stock belongs to.
        """
        stock_info = {}

        name = self.soup.select(
            "#top > div.flex.flex-space-between.flex-gap-8 > div > h1"
        )[0].text.strip()
        link = self.soup.select(
            "#top > div.company-links.show-from-tablet-landscape > a:nth-child(1)"
        )[0].attrs["href"]
        about = self.soup.select("#top .company-info .company-profile p")[0].text
        bse_link = self.soup.select(
            "#top > div.company-info > div.company-profile > div.company-links.hide-from-tablet-landscape.margin-top-20 > a:nth-child(2)"
        )[0].attrs["href"]
        try:
            nse_link = self.soup.select(
                "#top > div.company-info > div.company-profile > div.company-links.hide-from-tablet-landscape.margin-top-20 > a:nth-child(3)"
            )[0].attrs["href"]
        except:
            nse_link = ""

        # sector = self.soup.select("#peers")[0]
        # sector_industry = [
        #     term
        #     for term in re.split(
        #         "\s\s", sector.find_all(class_="sub")[0].text.replace("\n", "").strip()
        #     )
        #     if term != ""
        # ]
        
        sector = self.soup.select("#peers")[0]
        sub_links = sector.find("p", class_="sub").find_all("a")
        sector_industry = [link.text.strip() for link in sub_links]

        industry = sector_industry[1]
        sector = sector_industry[3]

        stock_info["name"] = name
        stock_info["about"] = about
        stock_info["link"] = link
        stock_info["bse_link"] = bse_link
        stock_info["nse_link"] = nse_link
        stock_info["sector"] = sector
        stock_info["industry"] = industry
        return stock_info

    def latest_price(self):
        price = (
            self.soup.select(
                "#top > div.flex.flex-space-between.flex-gap-8 > div > div.font-size-18.strong.line-height-14 > div.flex.flex-align-center > span:nth-child(1)"
            )[0]
            .text.strip()[1:]
            .strip()
        )
        return price

    def pros_and_cons(self):
        """
        Retrieves the pros and cons from the analysis section of the web page.

        :return: A dictionary containing the pros and cons as lists.
        :rtype: dict
        """
        pros = [item.text for item in self.soup.select("#analysis .pros li")]
        cons = [item.text for item in self.soup.select("#analysis .cons li")]
        pros_and_cons = {"pros": pros, "cons": cons}
        
        return pros_and_cons

    def basic_info(self):
        """
        Retrieves the basic information from the HTML page.

        :return: A dictionary containing the ratios and their corresponding values.
                 The keys are the names of the ratios and the values are the numbers associated with each ratio.
        """
        ratios_html = self.soup.select("#top-ratios li")
        ratios = {
            ratio.find_all(class_="name")[0]
            .text.strip(): ratio.find_all(class_="number")[0]
            .text.strip()
            for ratio in ratios_html
        }
        return ratios

    def financials(self, statement_name):
        """
        Retrieves the financial data for a given statement.

        Args:
            statement_name (str): The name of the statement to retrieve the financial data for.

        Returns:
            dict: A dictionary containing the financial data for the statement.
                - id (str): The ID of the statement.
                - title (str): The title of the statement.
                - content (dict): A dictionary containing the content of the statement.
                    - row_head (str): The header of a row in the statement.
                        - th[counter] (str): The column header.
                            - item (str): The value in the cell.

        """
        [table_id] = statement_name
        # ['quarters', 'profit-loss', 'balance-sheet', 'cash-flow', 'ratios', 'shareholding']

        title = self.soup.select(f"#{table_id} h2")[0].text.strip()  # Quarterly Results
        financial = {
            "id": table_id,
            "title": title,
            "content": {},
        }

        th = self.soup.select(f"#{table_id} table thead tr th")  # [<td> </td>]
        # ['', 'September 2021', 'September 2023']
        th = [head.text.strip() for head in th]
        col_num = len(th)  # 14
        # ['Sales', 12,903', '1234234', '13234']
        td = self.soup.select(f"#{table_id} table tbody td")

        counter = 0
        row_head = ""
        for cell in td:
            item = cell.text.strip()
            if counter == 0:
                financial["content"][item] = []
                row_head = item
                counter += 1
            elif counter == col_num:
                counter = 1
                financial["content"][item] = []
                row_head = item
            else:
                financial["content"][row_head].append({th[counter]: item})
                counter += 1

        return financial

    def profit_loss_statement(self):
        return self.financials(statement_name=["profit-loss"])

    def balance_sheet(self):
        return self.financials(statement_name=["balance-sheet"])

    def quarterly_statement(self):
        return self.financials(statement_name=["quarters"])

    def cash_flow_statement(self):
        return self.financials(statement_name=["cash-flow"])

    def common_ratios(self):
        return self.financials(statement_name=["ratios"])

    def shareholding_pattern(self):
        return self.financials(statement_name=["shareholding"])

    def company_announcements(self):
        announcements_li_items = self.soup.select("#company-announcements-tab li")
        document = {
            item.text.replace("\n", "").replace("  ", "").strip(): item.a["href"]
            for item in announcements_li_items
        }
        return document

    def documents(self, document_name):
        class_name = document_name
        # ['annual-reports', 'credit-ratings', 'concalls']

        document_html = self.soup.select(f"#documents .{class_name}")[0]
        title = document_html.h3.text.strip()
        li_items = document_html.find_all("li")
        document = {
            item.text.replace("\n", "").replace("  ", "").strip(): item.a["href"]
            for item in li_items
        }

        return document

    def annual_reports(self):
        """
        Retrieves the annual reports for the given company.

        :param self: The current instance of the class.
        :return: None
        """
        return self.documents("annual-reports")

    def credit_rating_reports(self):
        return self.documents("credit-ratings")

    def concalls(self):
        return self.documents("concalls")
