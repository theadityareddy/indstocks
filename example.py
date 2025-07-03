import indstocks as stocks

# Select the ticker
tickers = ['SBIN', 'LT', 'TCS', 'ZOMATO', 'MRF']
quote = stocks.Quote(tickers[0])


# print(quote.get_stock_info())
'''
{
  "name": "State Bank of India",
  "about": "State Bank of India is a Fortune 500 company. It is an Indian Multinational, Public Sector banking and financial services statutory body headquartered in Mumbai. It is the largest and oldest bank in India with over 200 years of history.[1]",
  "link": "http://www.sbi.co.in",
  "bse_link": "https://www.bseindia.com/stock-share-price/state-bank-of-india/SBIN/500112/",
  "nse_link": "https://www.nseindia.com/get-quotes/equity?symbol=SBIN",
  "sector": "Public Sector Bank",
  "industry": "Financial Services"
}
'''


# print(quote.get_current_price())
'''
811.40
'''


# print(quote.get_pros_and_cons())
'''
{
  "pros": [
    "Company has delivered good profit growth of 36.3% CAGR over last 5 years",
    "Company has been maintaining a healthy dividend payout of 18.2%"
  ],
  "cons": [
    "Company has low interest coverage ratio.",
    "Contingent liabilities of Rs.27,42,584 Cr.",
    "Earnings include an other income of Rs.1,72,406 Cr."
  ]
}
'''


# print(quote.get_basic_info())
'''
{
  "Market Cap": "7,23,787",
  "Current Price": "811",
  "High / Low": "899",
  "Stock P/E": "9.30",
  "Book Value": "546",
  "Dividend Yield": "1.96",
  "ROCE": "6.47",
  "ROE": "17.2",
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
  "Financial Year 2025from bse": "https://www.bseindia.com/stockinfo/AnnPdfOpen.aspx?Pname=9c6a98f8-f882-4c06-9cb1-7f3b6ae1159f.pdf",
  "Financial Year 2024from bse": "https://www.bseindia.com/stockinfo/AnnPdfOpen.aspx?Pname=0e236470-9427-43c7-93e9-c8eb61bb1f72.pdf",
  "Financial Year 2023from bse": "https://www.bseindia.com/stockinfo/AnnPdfOpen.aspx?Pname=\\22d33d1d-af2a-4d2d-98c0-eff16cd73cb5.pdf",
  "Financial Year 2022from bse": "https://www.bseindia.com/bseplus/AnnualReport/500112/73059500112.pdf",
  "Financial Year 2021from bse": "https://www.bseindia.com/bseplus/AnnualReport/500112/68518500112.pdf",
  "Financial Year 2020from bse": "https://www.bseindia.com/bseplus/AnnualReport/500112/5001120320.pdf",
  "Financial Year 2019from bse": "https://www.bseindia.com/bseplus/AnnualReport/500112/5001120319.pdf",
  "Financial Year 2018from bse": "https://www.bseindia.com/bseplus/AnnualReport/500112/5001120318.pdf",
  "Financial Year 2017from bse": "https://www.bseindia.com/bseplus/AnnualReport/500112/5001120317.pdf",
  "Financial Year 2016from bse": "https://www.bseindia.com/bseplus/AnnualReport/500112/5001120316.pdf",
  "Financial Year 2015from bse": "https://www.bseindia.com/bseplus/AnnualReport/500112/5001120315.pdf",
  "Financial Year 2014from bse": "https://www.bseindia.com/bseplus/AnnualReport/500112/5001120314.pdf",
  "Financial Year 2013from bse": "https://www.bseindia.com/bseplus/AnnualReport/500112/5001120313.pdf",
  "Financial Year 2012from bse": "https://www.bseindia.com/bseplus/AnnualReport/500112/5001120312.pdf",
  "Financial Year 2011from bse": "https://www.bseindia.com/bseplus/AnnualReport/500112/5001120311.pdf"
}
'''


# print(quote.get_market_depth())
'''
{
  "buy": [
    { "qty": "210", "price": "811.10" },
    { "qty": "477", "price": "811.05" },
    { "qty": "197", "price": "811.00" },
    { "qty": "28", "price": "810.90" },
    { "qty": "462", "price": "810.85" }
  ],
  "sell": [
    { "qty": "114", "price": "811.50" },
    { "qty": "185", "price": "811.55" },
    { "qty": "321", "price": "811.60" },
    { "qty": "356", "price": "811.65" },
    { "qty": "445", "price": "811.70" }
  ]
}
'''


# print(quote.get_stock_price_change())
'''
{'amount_change': -1.5, 'percent_change': -0.18, 'direction': 'down'}
'''


print(quote.get_broker_research())
'''
[
  {
    "name": "LKP Securities Limited",
    "date": "07 May, 2025",
    "reco_price": 776.15,
    "target_price": 907.0,
    "link": "https://images.moneycontrol.com/static-mcnews/2025/05/20250507043823_State-Bank-of-India-07052025-lkp.pdf"
  },
  {
    "name": "Motilal Oswal",
    "date": "04 May, 2025",
    "reco_price": 800.05,
    "target_price": 915.0,
    "link": "https://images.moneycontrol.com/static-mcnews/2025/05/20250505091411_State-Bank-of-India-05052025-moti.pdf"
  },
  {
    "name": "Emkay Global Financial Services",
    "date": "04 May, 2025",
    "reco_price": 800.05,
    "target_price": 975.0,
    "link": "https://images.moneycontrol.com/static-mcnews/2025/05/20250505071512_State-Bank-of-India-05052025-emkay.pdf"
  },
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
