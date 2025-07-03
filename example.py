import indstocks as stocks

# Select the ticker
tickers = ['SBIN', 'LT', 'TCS', 'ZOMATO', 'MRF']
quote = stocks.Quote(tickers[0])


print(quote.get_stock_info())
'''
{
  "name": "HDFC Bank Ltd",
  "about": "HDFC Bank Limited (also known as HDFC) is an Indian banking and financial services company headquartered in Mumbai. It is India's largest private sector bank by assets and the world's tenth-largest bank by market capitalization as of May 2024.\nAs of April 2024, HDFC Bank has a market capitalization of $145 billion, making it the third-largest company on the Indian stock exchanges. [1]",
  "link": "http://www.hdfcbank.com",
  "bse_link": "https://www.bseindia.com/stock-share-price/hdfc-bank-ltd/HDFCBANK/500180/",
  "nse_link": "https://www.nseindia.com/get-quotes/equity?symbol=HDFCBANK",
  "sector": "Financial Services",
  "industry": "Private Sector Bank"
}
'''


# print(quote.get_current_price())
'''
2,014.90
'''


# print(quote.get_pros_and_cons())
'''
{
  "pros": [
    "Company has delivered good profit growth of 21.0% CAGR over last 5 years",
    "Company has been maintaining a healthy dividend payout of 23.3%",
    "Company's median sales growth is 16.4% of last 10 years"
  ],
  "cons": [
    "Stock is trading at 2.98 times its book value",
    "Company has low interest coverage ratio.",
    "Contingent liabilities of Rs.24,09,821 Cr.",
    "Earnings include an other income of Rs.1,34,548 Cr."
  ]
}
'''


# print(quote.get_basic_info())
'''
{
  "Market Cap": "15,45,008",
  "Current Price": "2,015",
  "High / Low": "2,027",
  "Stock P/E": "21.8",
  "Book Value": "677",
  "Dividend Yield": "1.09",
  "ROCE": "7.51",
  "ROE": "14.5",
  "Face Value": "1.00"
}
'''


# print(quote.get_financials())
'''
Returns: Balance sheet, P&L, cash flow statements, and key ratios
'''


# print(quote.get_annual_reports())
'''
{
  "Financial Year 2024from bse": "https://www.bseindia.com/stockinfo/AnnPdfOpen.aspx?Pname=2160dea5-d49e-4409-83a4-c2b111a3bd12.pdf",
  "Financial Year 2023from bse": "https://www.bseindia.com/stockinfo/AnnPdfOpen.aspx?Pname=\\0fb0e6bd-7110-44c3-a750-76933ddf105c.pdf",
  "Financial Year 2022from bse": "https://www.bseindia.com/bseplus/AnnualReport/500180/73256500180.pdf",
  "Financial Year 2021from bse": "https://www.bseindia.com/bseplus/AnnualReport/500180/68609500180.pdf",
  "Financial Year 2020from bse": "https://www.bseindia.com/bseplus/AnnualReport/500180/5001800320.pdf",
  "Financial Year 2019from bse": "https://www.bseindia.com/bseplus/AnnualReport/500180/5001800319.pdf",
  "Financial Year 2018from bse": "https://www.bseindia.com/bseplus/AnnualReport/500180/5001800318.pdf",
  "Financial Year 2017from bse": "https://www.bseindia.com/bseplus/AnnualReport/500180/5001800317.pdf",
  "Financial Year 2016from bse": "https://www.bseindia.com/bseplus/AnnualReport/500180/5001800316.pdf",
  "Financial Year 2015from bse": "https://www.bseindia.com/bseplus/AnnualReport/500180/5001800315.pdf",
  "Financial Year 2014from bse": "https://www.bseindia.com/bseplus/AnnualReport/500180/5001800314.pdf",
  "Financial Year 2013from bse": "https://www.bseindia.com/bseplus/AnnualReport/500180/5001800313.pdf",
  "Financial Year 2012from bse": "https://www.bseindia.com/bseplus/AnnualReport/500180/5001800312.pdf",
  "Financial Year 2012from nse": "https://archives.nseindia.com/annual_reports/AR_HDFCBANK_2011_2012_20062012100212.zip",
  "Financial Year 2011from bse": "https://www.bseindia.com/bseplus/AnnualReport/500180/5001800311.pdf"
}
'''


# print(quote.get_market_depth())
'''
{
  "buy": [
    { "qty": "195", "price": "2011.50" },
    { "qty": "5", "price": "2011.45" },
    { "qty": "11", "price": "2011.05" },
    { "qty": "199", "price": "2010.05" },
    { "qty": "126", "price": "2010.00" }
  ],
  "sell": [
    { "qty": "10", "price": "2012.65" },
    { "qty": "45", "price": "2012.95" },
    { "qty": "36", "price": "2013.00" },
    { "qty": "392", "price": "2013.40" },
    { "qty": "651", "price": "2013.45" }
  ]
}
'''


# print(quote.get_stock_price_change())
'''
{ "amount_change": -6.9, "percent_change": -0.34, "direction": "down" }
'''


# print(quote.get_broker_research())
'''
[
  {
    "name": "Geojit Financial Services",
    "date": "06 May, 2025",
    "reco_price": 1930.55,
    "target_price": 2192.0,
    "link": "https://images.moneycontrol.com/static-mcnews/2025/05/20250514084746_HDFC-Bank-14052025-geo.pdf"
  },
  {
    "name": "Sharekhan",
    "date": "19 Apr, 2025",
    "reco_price": 1906.55,
    "target_price": 2300.0,
    "link": "https://images.moneycontrol.com/static-mcnews/2025/04/20250422070215_HDFC-Bank-22042025-khan.pdf"
  },
  {
    "name": "Emkay Global Financial Services",
    "date": "20 Apr, 2025",
    "reco_price": 1906.55,
    "target_price": 2200.0,
    "link": "https://images.moneycontrol.com/static-mcnews/2025/04/20250421124117_HDFC-Bank-21042025-emkay.pdf"
  },
  {
    "name": "ICICI Securities",
    "date": "20 Apr, 2025",
    "reco_price": 1906.55,
    "target_price": 2200.0,
    "link": "https://images.moneycontrol.com/static-mcnews/2025/04/20250421082856_HDFC-Bank-21042025-icici.pdf"
  },
  {
    "name": "Motilal Oswal",
    "date": "20 Apr, 2025",
    "reco_price": 1906.55,
    "target_price": 2200.0,
    "link": "https://images.moneycontrol.com/static-mcnews/2025/04/20250421081425_HDFC-Bank-21042025-moti.pdf"
  },
  {
    "name": "Prabhudas Lilladher",
    "date": "21 Apr, 2025",
    "reco_price": 1927.55,
    "target_price": 2125.0,
    "link": "https://images.moneycontrol.com/static-mcnews/2025/04/20250421062752_HDFC-Bank-21042025-prabhu.pdf"
  }
]
'''


# print(quote.get_top_news())
'''
Returns: Article title, link, publication date
'''

# print(quote.get_stock_historical_data())
'''
Returns: Historical price and volume data
'''


# print(quote.get_all_stock_data())
'''
Returns : All of the above in JSON format
'''
