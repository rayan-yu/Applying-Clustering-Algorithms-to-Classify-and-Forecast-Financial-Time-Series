import pandas as pd
import pandas_datareader as pdr
import pandas_datareader.data as web
import datetime
import time
import statistics

# read an array of tickers
ticker_csv = 'C:/ry_sci/demo/nasdaq_ticker.csv'
tickers = pd.read_csv(ticker_csv, usecols =['Symbol']) 
symbol = tickers['Symbol'].values

# filters: time range
start = datetime.date(2017,1,1)
end = datetime.date(2017,12,31)
# filters: volume smaller than 500000
volume_condition = 500000

#set path for price csv file
path_out = 'C:/ry_sci/demo/'
csv_out = 'tickers.csv'

# generate a csv file with stock tickers and their price time series
print("processing...", time.asctime( time.localtime(time.time()) ))
i=0
no_data = 0;
counter = 0;

while i<len(symbol):
#while i < 50:
    try:
		# Date, High,	Low,	Open,	Close,	Volume,	Adj Clos
        df = web.DataReader(symbol[i], 'yahoo', start, end)
		if statistics.mean(df['Volume']) < volume_condition:
			i=i+1
			continue
        df_tr = df.T
        df = df_tr['Adj Close':]# this stock's adj close price time series as a numpy array
        df.insert(0, 'Symbol', symbol[i])
        df.set_index('Symbol')
    
        if i == 0:
            df.to_csv(path_out + csv_out)
            print (i, symbol[i],'has data stored to csv file')
        else:
            df.to_csv(path_out + csv_out,mode = 'a', header=False)
            print (i, symbol[i],'has data stored to csv file')
		counter = counter + 1
    except:
        #print("No information for ticker # and symbol:")
        #print (i,symbol[i])
        no_data = no_data + 1;
        i=i+1
        continue
    i=i+1
print("There are ", no_data, " stocks that no longer exist.")
print("Processed ", counter, " stockers, all with avg volume greater than ", volume_condition)
print("done...", time.asctime( time.localtime(time.time()) ))