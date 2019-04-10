import os
import pandas as pd

path_proj = 'C:/ry_sci/'
path_data = path_proj + 'data/'
data_folder = 'SP500_2018_daily' # 'SP500_2018_30min', 'SP500_2018_daily', 'SP500_2018_5min'
data_pathfolder = path_data + data_folder

sp_csv = os.listdir(data_pathfolder) # list all price files in the folder
i=0
df = pd.DataFrame()
while i < len(sp_csv):
    print('processing ', sp_csv[i])
    
    # df2 = pd.read_csv(data_pathfolder + '/' + sp_csv[i])
    # Date,Time,Open,High,Low,Close,Volume
	
    ###################### multi index
    #df2 = pd.read_csv(data_pathfolder + '/' + sp_csv[i], index_col=['Date', 'Time']) 
    ###################### single datetime index
    df2 = pd.read_csv(data_pathfolder + '/' + sp_csv[i], usecols=[0, 1, 6], dtype={0:'str',1:'int64',6:'int64'}, skipfooter=1, engine='python')
    df2['DateTime'] = df2['Date'].astype(str).str.cat(df2['Time'].astype(str), sep=' ')
    df2['DateTime'] = pd.to_datetime(df2['DateTime'], format='%m/%d/%Y %H%M')
    df2 = df2.set_index('DateTime') # make the combined date and time columns as the index
    price_series = df2['Close'] # this stock's close price time series as a series
    df2 = pd.DataFrame(price_series) # make the time series into a dataframe, one stock time series a column
    ticker = sp_csv[i].split('_', 2)[0] # take the file name as ticker symbol, e.g. AAA_period.txt, the symbol will be AAA
    df2 = df2.rename(index=str, columns={"Close": ticker }) # set the column name as ticker

    if i == 0:
        df = df2 # first ticker price series as first column
        print (i, 'has data stored to csv file')
    else:
        df = pd.concat([df, df2], axis=1, sort=False) # add additional ticker series as columns
        print (i, sp_csv[i],'has data stored to csv file')
    i = i+1
df.to_csv(data_pathfolder + "_time_rows.csv") # time as rows

# df_tr = df.T # transform the column into a row
# df_tr = df_tr.dropna() # drop the ticker row
# df_tr.index.name = "Symbol" # set the index column to ticker name
# df_tr.to_csv(path_proj + data_folder + "_ticker_rows.csv") # each ticker time series as rows, output into a csv file
