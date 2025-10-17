# This file replaces the scappring of investing.com
# with the use of internal api of investing.com to 
# make the historical data functions reavailable
from curl_cffi import requests
import json
from bs4 import BeautifulSoup
import importlib.resources

class InternalAPI:
    def __init__(self,ticker):
        base_headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'cross-site',
            'Priority': 'u=0, i',
            'TE': 'trailers'
        }
        self.session = session = requests.Session()
        self.session.headers.update(base_headers)
        self.ticker = ticker
        with importlib.resources.open_text("indstocks.scrapers", "links.json") as file:
            link_dict = json.load(file)
        base_URL = link_dict[self.ticker]["investing_link"]
        self.URL = base_URL + "-historical-data"

    def _get_pair_by_url(self,html, target_url)->int:
        """
        Internal function to get pair id of a stock. Further use in internal api
        :param: 
            html : A valid investing.com html code | Example: https://in.investing.com/equities/3m-india-historical-data
            target_url : A valid investing.com url | Example: https://in.investing.com/equities/3m-india-historical-data
        :return : stock id
        """
        soup = BeautifulSoup(html, "html.parser")

        script_tag = soup.find("script", id="__NEXT_DATA__")
        if not script_tag:
            raise ValueError("Could not find __NEXT_DATA__ script tag")

        data = json.loads(script_tag.string)
        scoped_data = data["props"]["pageProps"]["state"]["quotesStore"]["quotes"]

        stock_id = None
        for x in scoped_data:
            for y in x:
                if type(y) == str:
                    pass
                else:
                    for i in y["_collection"]:
                        try:
                            if i["url"] == target_url:
                                stock_id = int(i["pair"])
                        except:
                            pass
        if stock_id == None:
            raise ValueError(f"Stock paring id not found")
        else:
            return stock_id
    
    def _get_home_html_code(self)->str:
        """This is a internal function to return the html code of the page"""
        url = self.URL
        response = self.session.get(url,impersonate="chrome110")
        if response.status_code == 200:
            return str(response.text)
        else:
            return None
    
    def _get_short_target_url(self)->str:
        url = self.URL
        url_split = url.split("in.investing.com")
        url_split2 = url_split[1].split("-historical-data")
        return str(url_split2[0])
    
    def historical_data(self):
        html = self._get_home_html_code()
        target_url = self._get_short_target_url()
        

        pair_id = self._get_pair_by_url(
            html = html,
            target_url = target_url
        )

        api_url = f"https://api.investing.com/api/financialdata/historical/{pair_id}?start-date=2025-08-18&end-date=2025-09-16&time-frame=Daily&add-missing-rows=false"
        self.session.headers.update({
            'Referer': 'https://in.investing.com/',
            'domain-id': 'in',
            'Origin': 'https://in.investing.com',
        })
        response = self.session.get(api_url,impersonate="chrome110")
        
        if response.status_code == 200:
            return response.text
        else:
            print(f"Request failed with status code: {response.status_code}")



