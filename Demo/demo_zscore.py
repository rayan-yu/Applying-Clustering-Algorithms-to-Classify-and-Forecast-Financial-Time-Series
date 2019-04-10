# zscore examples
import numpy as np
import pandas as pd
from scipy import stats
import numpy.random as random

# on an array 1-dimensional
a = np.array([ 0.3148,  0.0478,  0.6243,  0.4608])
stats.zscore(a)

# Computing along a specified axis, using n-1 degrees of freedom (ddof=1) to calculate the standard deviation:
b = np.array([[ 0.3148,  0.0478,  0.6243,  0.4608], \
               [ 0.7149,  0.0775,  0.6072,  0.9656], \
               [ 0.6341,  0.1403,  0.9759,  0.4064], \
               [ 0.5918,  0.6948,  0.904 ,  0.3721], \
               [ 0.0921,  0.2481,  0.1188,  0.1366]])
stats.zscore(b)
stats.zscore(b, axis=1) # row by row
stats.zscore(b, axis=1, ddof=1)

random.seed(1234)
c = [random.random() for _ in range(10)]
stats.zscore(c, axis=1)

# obtain a zscore matrix on a matrix, keep the index and columns
df = pd.DataFrame(np.random.randn(10, 4), columns=['A', 'B', 'C', 'D'])
dfz = stats.zscore(df, axis=1)
dfz = pd.DataFrame(dfz, index=df.index, columns=df.columns)
D2 = pairwise_distances(dfz, metric='euclidean')
pd.DataFrame(D2) # all diagonals are zero's