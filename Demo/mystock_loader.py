import pandas as pd
import pandas_datareader as pdr
import pandas_datareader.data as web
import datetime

# get list of tickers and save to ticker csv file
ticker_csv = 'c:/ry_sci/demo/nasdaq_ticker.csv'
df = pdr.nasdaq_trader.get_nasdaq_symbols(retry_count=3, timeout=30, pause=None)
df.to_csv(ticker_csv)

# an array of tickers
# tickers = pd.read_csv(ticker_csv, usecols =['Symbol']) 
symbol = tickers['Symbol'].values

#datetime is a Python module
 
#datetime.datetime is a data type within the datetime module
#which allows access to Gregorian dates and today function
 
#datetime.date is another data type within the datetime module
#which permits arithmetic with Gregorian date components
 
#definition of end with datetime.datetime type must precede
#definition of start with datetime.date type
 
#the start expression collects data that are up to five years old, e.g. endyear-5
 
end = datetime.datetime.today()
 
start = datetime.date(end.year-1,1,1)
 
#set path for csv file
path_out = 'C:/ry_sci/demo/'
csv_out = 'yahoo_prices_volumes_for_ST_50_to_csv_demo.csv'
 
#loop through 50 tickers in symbol list with i values of 0 through 49
 
#if no historical data returned on any pass, try to get the ticker data again
 
#for first ticker symbol write a fresh copy of csv file for historical data
#on remaining ticker symbols append historical data to the file written for
#the first ticker symbol and do not include a header row
 
i=0
#while i<len(symbol):
while i<10:
    try:
        df = web.DataReader(symbol[i], 'yahoo', start, end)
        df.insert(0,'Symbol',symbol[i])
        df = df.drop(['Adj Close'], axis=1)
        if i == 0:
            df.to_csv(path_out + csv_out)
            print (i, symbol[i],'has data stored to csv file')
        else:
            df.to_csv(path_out + csv_out,mode = 'a', header=False)
            print (i, symbol[i],'has data stored to csv file')
    except:
        print("No information for ticker # and symbol:")
        print (i,symbol[i])
        continue
    i=i+1
