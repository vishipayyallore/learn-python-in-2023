import yfinance as yf

#define the ticker symbol
tickerSymbol = 'MSFT'

#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
print(tickerData)

print('Stock price of MSFT: ', tickerData.info['currentPrice'])
