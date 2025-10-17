import json
import importlib.resources
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time



class Investing:
    def __init__(self, ticker):
        self.ticker = ticker
        with importlib.resources.open_text("indstocks.scrapers", "links.json") as file:
            link_dict = json.load(file)
        base_URL = link_dict[self.ticker]["investing_link"]
        self.URL = base_URL + "-historical-data"

    def page_html(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        driver = webdriver.Chrome(options=options)
        driver.get(self.URL)

        # Wait for 5 seconds instead of waiting for an element
        time.sleep(5)

        html = driver.page_source

        # Save the HTML to a file for debugging
        with open("test.html", "w", encoding="utf-8") as f:
            f.write(html)
        print("Saved HTML to test.html")

        driver.quit()
        return html

    def historical_price(self):
        soup = BeautifulSoup(self.page_html(), "html.parser")
        table = soup.find("table", class_="common-table medium js-table")
        rows = table.find_all("tr", class_="common-table-item u-clickable")

        historical_data = {
            "date": [],
            "price": [],
            "open": [],
            "high": [],
            "low": [],
            "volume": [],
            "change": [],
        }

        for row in rows:
            cols = row.find_all("td")
            historical_data["date"].append(cols[0].text.strip())
            historical_data["price"].append(self.string_to_num(cols[1].text))
            historical_data["open"].append(self.string_to_num(cols[2].text))
            historical_data["high"].append(self.string_to_num(cols[3].text))
            historical_data["low"].append(self.string_to_num(cols[4].text))
            historical_data["volume"].append(self.string_to_num(cols[5].text))
            historical_data["change"].append(self.string_to_num(cols[6].text))

        return historical_data

    def string_to_num(self, str_val):
        try:
            return float(str_val.strip().replace(",", "").replace("%", ""))
        except (ValueError, TypeError):
            return str_val
