#import numpy as np
#import pandas as pd
#from scipy import stats
#stock_prices_csv = 'C:/ry_sci/demo/tickerprice_demo.csv'
#df = pd.read_csv(stock_prices_csv, index_col=[0, 'Symbol'], header=0)
#dz = stats.zscore(df)
#dfz = pd.DataFrame(dz, index=df.index, columns=df.columns)

import numpy as np
import pandas as pd
from scipy import stats
stock_prices_csv = 'C:/ry_sci/demo/tickerprice_demo.csv'
df = pd.read_csv(stock_prices_csv, index_col=['Symbol'], header=0)
df = df.drop(columns=['Unnamed: 0'])
dz = stats.zscore(df)
dfz= pd.DataFrame(dz, index=df.index, columns=df.columns)
