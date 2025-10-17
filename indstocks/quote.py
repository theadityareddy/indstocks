# Get the quote details
# - current price, company info, etc.

from indstocks.scrapers import Investing, MoneyControl, Screener,InternalAPI
import json
import datetime as dt
from typing import Dict

class Quote:
    def __init__(self, ticker):
        # print("Invoked Quote module...")
        self.screener = Screener(ticker=ticker)
        self.screener.get_soup()
        self.mc = MoneyControl(ticker=ticker)
        self.mc.get_soup()
        self.investing = Investing(ticker=ticker)
        self.internalAPI = InternalAPI(ticker=ticker)

    def get_all_stock_data(self,indent:int=None)->Dict:
        """
        Retrieves all stock data for a given stock.

        :param self: The instance of the class.
        :pram indent: Indentation of dict/json , default None
        :return: A dictionary containing various stock data such as current price, basic info, description,
                 historical data, price change, market depth, broker research, pros and cons, financials,
                 annual reports, and top news.
        """
        data = {
            "current_price": self.get_current_price(),
            "basic_info": self.get_basic_info(),
            "description": self.get_stock_info(),
            #"historical_data": self.get_historical_data(),
            "price_change": self.get_stock_price_change(),
            "market_depth": self.get_market_depth(),
            "broker_research": self.get_broker_research(),
            "pros_and_cons": self.get_pros_and_cons(),
            "financials": self.get_financials(),
            "annual_reports": self.get_annual_reports(),
            "top_news": self.get_top_news(),
        }
        all_data = json.dumps(data,indent=indent)
        return all_data

    def get_current_price(self):
        """
        Get the current price.

        Returns:
            The current price.

        """
        # print("Getting current price")
        return self.mc.current_price()

    def get_stock_info(self):
        """
        Retrieves the stock information for a company.

        Returns:
            The stock information for the company.
        """
        # print("Getting company information")
        return self.screener.stock_information()  # only gets company desc

    def get_stock_historical_data(self):
        """
        Retrieves the historical data for a stock.

        Returns:
            The historical price data for the stock.
        """
        # print("Getting stock historical data")
        return self.internalAPI.historical_data()

    def get_stock_price_change(self):
        """
        Get the stock price change.

        :return: The stock price change.
        """
        # print("Getting stock price change")
        return self.mc.price_change()

    def get_market_depth(self):
        """
        Get the market depth.

        Returns:
            The market depth.
        """
        # print("Getting market depth")
        return self.mc.market_depth()

    def get_broker_research(self):
        """
        Retrieves the broker research data from the `mc` object.

        Returns:
            The broker research data obtained from the `mc` object.
        """
        # print("Getting broker research")
        return self.mc.broker_research()

    def get_pros_and_cons(self):
        """
        Get the pros and cons of the screener.

        Returns:
            The pros and cons of the screener.
        """
        # print("Getting pros and cons")
        return self.screener.pros_and_cons()

    def get_basic_info(self):
        """
        Returns the basic information by calling the `basic_info()` method of the `screener` object.

        Parameters:
            self (object): The instance of the class.

        Returns:
            object: The basic information obtained from the `basic_info()` method.
        """
        # print("Getting basic info")
        return self.screener.basic_info()

    def get_financials(self):
        """
        Get the financial statements for the current stock.

        Returns:
            dict: A dictionary containing the profit and loss statement and cash flow statement.
        """
        # print("Getting financials")
        financials = {
            "bs": self.screener.balance_sheet(),
            "pnl": self.screener.profit_loss_statement(),
            "cashflow": self.screener.cash_flow_statement(),
            "common_ratios": self.screener.common_ratios(),
        }
        return financials

    def get_annual_reports(self):
        """
        Retrieves the annual reports from the screener.

        Returns:
            A list of annual reports.
        """
        # print("Getting annual reports")
        return self.screener.annual_reports()

    def get_top_news(self):
        """
        Fetches the top news from the `mc` object.

        Returns:
            The top news fetched from the `mc` object.
        """
        # print("Getting top news")
        return self.mc.top_news()

if __name__ == "__main__":
    quote = Quote("HDFC")
    cur = quote.get_current_price()
    print(cur)
