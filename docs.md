# Data being fetched:

### SCREENER

- About the company (Brief, Sector, Industry, Name, Link to Website, BSE Link, NSE Link)
- Pros & Cons (Machine Generated)
- Key Highlights - Market Cap, Current Price, High/ Low Price, P/E, Book Value, Dividend Yield, ROCE, ROE, Face Value
- Consolidated Quarterly Results
- Consolidated P&L
- Consolidated B/S
- Consolidated Cash Flow
- Ratios - Debtor Days, Inventory Days, Days Payable, Cash Conversion Cycle, ROCE etc
- Shareholding Pattern
- Announcement, Annual Reports, Credit Rating, Concall PPTs

### MONEY CONTROL

- Current Price (delayed)
- Top News
- Market Depth
- Broker Research

### TradingView

- Real Time Ticker
- Historical Price Data (Price, Vol, Open, Close)

### Investing

- Historical Price Data - Price

* financials : array of tables \*
  ''' financials = [
  {
  "id": "table_id",
  "title": "NAME",
  "content": {
  "row_header_1": [
  {"column_header": "cell_value"},
  {"column_header": "cell_value"}
  ],
  "row_header_2": [
  {"column_header": "cell_value"},
  {"column_header": "cell_value"}
  ]
  },
  },
  {
  "id": "table_id",
  "title": "Quarterly Financials",
  "content": {
  "Revenues": [
  {"Sept'21": 123},
  {"March'21": 456}
  ],
  "Expense": [
  {"Sept'21": 123},
  {"March'21": 456}]
  },
  },
  {},
  ]'''
