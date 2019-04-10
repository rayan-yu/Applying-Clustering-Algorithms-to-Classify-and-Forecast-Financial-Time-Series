#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
from scipy import stats
import random
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import pairwise_distances

################################################################
# Calculate KMeans clusters
#
#
stock_prices_csv = 'C:/ry_sci/demo/tickerprice_demo.csv'
df = pd.read_csv(stock_prices_csv, index_col=['Symbol'], header=0)

# calculate zscore
dz = stats.zscore(df, axis=1)
dfz= pd.DataFrame(dz, index=df.index, columns=df.columns)

# decide the k number using elbow method
import matplotlib.pyplot as plt
import pandas as pd
sse_ = []
for k in range(1, 40):
    kmeans = KMeans(n_clusters=k).fit(dfz)
    sse_.append([k, kmeans.inertia_])
plt.plot(pd.DataFrame(sse_)[0], pd.DataFrame(sse_)[1]);

# calculate kmeans clustering
k = 3 # number of clusters, will use elbow method to decide k
print("Used K number: ", k)
kmeans = KMeans(n_clusters=k).fit(dfz)
centers = kmeans.cluster_centers_

# output each cluster tickers, sorted by distance
centers = np.array(kmeans.cluster_centers_) # 
num_closest = 3 # number of closest tickers
dist = kmeans.transform(dfz) # transform to distance matrix
print("distance matrix\n", dist)

for i in range(k):
    d = dist[:, i] # distance array of the cluster i
    ind = np.argsort(d)[::][:num_closest] # an array of indices that are sorted by distance to the cluster center
    print("cluster ", i, ":", ind)
    for j in range(num_closest):
        print("row #", ind[j], ": ", dfz.iloc[ind[j]].name) # ind[j] is the row number, name is the row's (Series) ticker
