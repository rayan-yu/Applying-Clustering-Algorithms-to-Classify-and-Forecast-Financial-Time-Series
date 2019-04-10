import os
import pandas as pd

path_out = 'C:/ry_sci/data/SP500 Daily 12 Yr to 11262018/'
csv_out = '12y_prices.csv'
sp_csv = os.listdir(path_out + 'Stocks') # list all price files in the folder
i=0
while i < len(sp_csv):
    print('processing ', sp_csv[i])
    df = pd.read_csv(path_out + 'Stocks/' + sp_csv[i], index_col=['Date'])
    price_series = df['Close'] # this stock's close price time series as a series
    df = pd.DataFrame(price_series) # make the time series into a dataframe, one stock a row
    df_tr = df.T
    df = df_tr
    ticker = sp_csv[i].split('.', 2)[0] # take the file name as ticker symbol, e.g. AAA.txt, the symbol will be AAA
    df.insert(0, 'Symbol', ticker) # add ticker as Symbol column
    df.set_index('Symbol')
    if i == 0:
        df.to_csv(path_out + csv_out)
        print (i, 'has data stored to csv file')
    else:
        df.to_csv(path_out + csv_out,mode = 'a', header=False)
        print (i, sp_csv[i],'has data stored to csv file')
    i = i+1