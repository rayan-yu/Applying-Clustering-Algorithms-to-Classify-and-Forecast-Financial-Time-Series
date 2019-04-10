# distance matrix on an array

import numpy as np
a = np.array([ 0.7972,  0.0767,  0.4383,  0.7866,  0.8091, 0.1954,  0.6307,  0.6599,  0.1065,  0.0508])
from scipy import stats
dist_matrix = stats.zscore(a)
dist_matrix

# distance matrix on a data frame
import pandas as pd

# generate a data frame 10x5
d = pd.DataFrame(a)
i=1
while i < 5:
    b = [np.random.random() for _ in range(10)]
    d.insert(i, i, b)
    i= i+1
	
dist_matrix = stats.zscore(d)
dist_matrix