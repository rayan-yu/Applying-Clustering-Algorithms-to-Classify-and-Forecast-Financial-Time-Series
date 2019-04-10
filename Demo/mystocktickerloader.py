import pandas_datareader as pdr

# save a csv file of tickers
ticker_csv = 'C:/ry_sci/demo/nasdaq_ticker.csv'
df = pdr.nasdaq_trader.get_nasdaq_symbols(retry_count=3, timeout=30, pause=None)
df.to_csv(ticker_csv)
