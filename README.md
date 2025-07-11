# INDStocks: Python Library for Indian Stock Market Data & Analysis

[![PyPI - Version](https://img.shields.io/pypi/v/indstocks)](https://pypi.org/project/indstocks/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Downloads](https://static.pepy.tech/badge/indstocks)](https://pepy.tech/project/indstocks)
[![Monthly Downloads](https://static.pepy.tech/badge/indstocks/month)](https://pepy.tech/project/indstocks)
[![Weekly Downloads](https://static.pepy.tech/badge/indstocks/week)](https://pepy.tech/projects/indstocks)

---

## 📦 Installation

```bash
pip install indstocks
```

A comprehensive, developer-friendly Python package for real-time and historical Indian stock market data, company fundamentals, financial statements, analyst research, and more. INDStocks aggregates data from top sources making it the go-to toolkit for investors, analysts, and developers working with Indian equities.

---

## 📚 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Supported Tickers](#supported-tickers)
- [API Reference](#api-reference)
  - [Quote Class](#quote-class)
  - [Method Reference](#method-reference)
- [Sample Outputs](#sample-outputs)
- [Data Sources](#data-sources)
- [Usage Examples](#usage-examples)
- [Requirements](#requirements)
- [Legal & Compliance](#legal--compliance)
- [Contributing](#contributing)
- [Support](#support)

---

## Overview

**INDStocks** is an all-in-one Python library for Indian stock market data. It provides:
- Real-time and historical prices
- Company fundamentals and financials
- Analyst research and news
- Market depth and order book
- AI-generated investment pros & cons
- Direct links to annual reports

INDStocks is ideal for:
- Quantitative research
- Portfolio analysis
- Financial modeling
- Investment screening
- Educational and academic use

---

## Features

- **Live Stock Prices**: Fetch up-to-date prices for any NSE/BSE-listed company.
- **Market Depth**: Access real-time order book (buy/sell) data.
- **Company Fundamentals**: Instantly retrieve market cap, P/E, book value, dividend yield, ROCE, ROE, and more.
- **Financial Statements**: Download balance sheets, profit & loss, cash flow, and key ratios.
- **Broker Research**: Get the latest analyst reports, target prices, and recommendations.
- **News & Announcements**: Stay updated with top news and company announcements.
- **Pros & Cons**: AI-generated investment thesis, highlighting strengths and risks.
- **Annual Reports**: Direct links to official annual reports from BSE/NSE.
- **Historical Data**: Download price, volume, and technical data for backtesting and analysis.
- **Multi-source Aggregation**: Combines data from MoneyControl, Screener, Investing.com, and more.

---

## Installation

```bash
pip install indstocks
```

Or, for the latest development version:

```bash
git clone https://github.com/theadityareddy/indstocks
cd indstocks
python setup.py install
```

---

## Quick Start

```python
import indstocks as stocks

quote = stocks.Quote("SBIN")

print("Current Price:", quote.get_current_price())
print("Company Info:", quote.get_stock_info())
```

---

## Supported Tickers

INDStocks supports hundreds of NSE/BSE tickers. Some popular examples include:

- `SBIN`, `RELIANCE`, `MRF`, `INFY`, `ZOMATO`, `HDFCBANK`, `ITC`, `KOTAKBANK`, `ICICIBANK`, `LT`

For the full list, see the [`indstocks/scrapers/links.json`](indstocks/scrapers/links.json) file in the repository.

---

## API Reference

### Quote Class

The `Quote` class is the main entry point for all stock data. Initialize it with a valid ticker symbol:

```python
from indstocks import Quote
quote = Quote("MRF")
```

### Method Reference

Each method returns data as a Python object (dict, list, or value). Most methods raise a `ValueError` if the ticker is invalid or data is unavailable.

| Method | Description | Return Type |
|--------|-------------|------------|
| `get_current_price()` | Latest stock price | `float` or `str` |
| `get_stock_info()` | Company profile, sector, industry, links | `dict` |
| `get_basic_info()` | Key financial ratios and metrics | `dict` |
| `get_financials()` | Balance sheet, P&L, cash flow, ratios | `dict` |
| `get_market_depth()` | Real-time order book (buy/sell) | `dict` |
| `get_stock_price_change()` | Price change (amount, percent, direction) | `dict` |
| `get_broker_research()` | Analyst reports and targets | `list[dict]` |
| `get_pros_and_cons()` | AI-generated investment thesis | `dict` |
| `get_annual_reports()` | Links to annual reports | `dict` |
| `get_top_news()` | Latest news headlines | `list[dict]` |
| `get_stock_historical_data()` | Historical price and volume data | `dict` |
| `get_all_stock_data()` | All of the above in one call | `dict` |

#### Error Handling
- If a ticker is not found, methods raise a `ValueError`.
- If a data source is temporarily unavailable, methods may return `None` or raise an exception.
- Always check for `None` or handle exceptions in production code.

---

## Sample Outputs

### `get_stock_info()`
```json
{
  "name": "State Bank of India",
  "about": "State Bank of India is a Fortune 500 company. It is an Indian Multinational, Public Sector banking and financial services statutory body headquartered in Mumbai. It is the largest and oldest bank in India with over 200 years of history.[1]",
  "link": "http://www.sbi.co.in",
  "bse_link": "https://www.bseindia.com/stock-share-price/state-bank-of-india/SBIN/500112/",
  "nse_link": "https://www.nseindia.com/get-quotes/equity?symbol=SBIN",
  "sector": "Public Sector Bank",
  "industry": "Financial Services"
}
```

### `get_current_price()`
```json
811.40
```

### `get_pros_and_cons()`
```json
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
```

### `get_basic_info()`
```json
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
```

### `get_market_depth()`
```json
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
```

### `get_broker_research()`
```json
[
  {
    "name": "Motilal Oswal",
    "date": "04 May, 2025",
    "reco_price": 800.05,
    "target_price": 915.0,
    "link": "https://images.moneycontrol.com/static-mcnews/2025/05/20250505091411_State-Bank-of-India-05052025-moti.pdf"
  }
]
```

---

## Data Sources

INDStocks aggregates and harmonizes data from multiple trusted sources:
- **Screener**: Company fundamentals, ratios, annual reports
- **Investing.com**: Real-time and historical prices
- **MoneyControl**: Financial statements, news, broker research, market depth

---

## Usage Examples

### Portfolio Analysis
```python
from indstocks import Quote

portfolio = ['MRF', 'LT', 'TCS', 'ZOMATO', 'SBIN']
results = {}

for ticker in portfolio:
    stock = Quote(ticker)
    results[ticker] = {
        "price": stock.get_current_price(),
        "change": stock.get_stock_price_change(),
        "pe_ratio": stock.get_basic_info().get("Stock P/E"),
        "target_price": (
            stock.get_broker_research()[0]["target_price"]
            if stock.get_broker_research()
            else None
        )
    }

print(results)
```

### Investment Research Workflow
```python
def research_stock(ticker):
    stock = Quote(ticker)
    basics = stock.get_basic_info()
    profile = stock.get_stock_info()
    thesis = stock.get_pros_and_cons()
    research = stock.get_broker_research()
    
    avg_target = (
        sum(r['target_price'] for r in research) / len(research)
        if research else None
    )

    return {
        "company": profile.get("name"),
        "sector": profile.get("sector"),
        "current_price": stock.get_current_price(),
        "analyst_target": avg_target,
        "investment_thesis": thesis
    }


report = research_stock('MRF')

print(report)
```

---

## Requirements

- Python 3.7+
- Internet connection for real-time data
- Dependencies are automatically installed via pip

---

## Legal & Compliance

INDStocks uses publicly available financial data. Users are responsible for:

- Complying with **data source terms**
- Respecting **rate limits & scraping policies**
- Avoiding commercial misuse

> 📌 Always verify data before using for trading or investment decisions.

---

## Contributing

INDStocks is **open source** and we welcome all kinds of contributions!

👨‍💻 To contribute:
- Fork the [GitHub repo](https://github.com/theadityareddy/indstocks)
- Submit pull requests, bug reports, or suggestions
- Improve documentation or add new sources

---

## Support

📄 **Docs**: This README is your main guide  
🐞 **Issues**: Use GitHub [Issues](https://github.com/theadityareddy/indstocks/issues)  
💬 **Community**: Join in, suggest features, and help improve!

---

**Disclaimer**: This tool is for research, educational, and non-commercial use only. Always verify financial data before making investment decisions.