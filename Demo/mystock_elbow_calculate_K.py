#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from scipy import stats

################################################################
# Calculate KMeans clusters
#
#
path_proj = 'C:/ry_sci/'
path_data = path_proj + 'data/'
data_folder = 'SP500_2018_daily' # 'SP500_2018_30min', 'SP500_2018_daily', 'SP500_2018_5min'

stock_prices_csv = path_data + data_folder + '_ticker_rows.csv' # the csv file of the stock price matrix
print("Reading the stock price matrix csv file...", stock_prices_csv)
# read the csv matrix file
df = pd.read_csv(stock_prices_csv, index_col=['Symbol'], header=0)

# calculate zscore
print("Calculating the zscore...")
dz = stats.zscore(df, axis=1)
dfz= pd.DataFrame(dz, index=df.index, columns=df.columns)

# decide the k number using elbow method
print("Clustering...")
sse_ = []
for k in range(1, 20):
    kmeans = KMeans(n_clusters=k).fit(dfz)
    sse_.append([k, kmeans.inertia_])
print("Finding the best K...")
# plt.plot(pd.DataFrame(sse_)[0], pd.DataFrame(sse_)[1])

# find the farthest point on the curve from the first and the last curve lines
define best_k(curve):
	nPoints = len(curve)
	allCoord = np.vstack((range(nPoints), curve)).T
	np.array([range(nPoints), curve])
	firstPoint = allCoord[0]
	lineVec = allCoord[-1] - allCoord[0]
	lineVecNorm = lineVec / np.sqrt(np.sum(lineVec**2))
	vecFromFirst = allCoord - firstPoint
	scalarProduct = np.sum(vecFromFirst * np.matlib.repmat(lineVecNorm, nPoints, 1), axis=1)
	vecFromFirstParallel = np.outer(scalarProduct, lineVecNorm)
	vecToLine = vecFromFirst - vecFromFirstParallel
	distToLine = np.sqrt(np.sum(vecToLine ** 2, axis=1))
	idxOfBestPoint = np.argmax(distToLine)
	k =  idxOfBestPoint+1
	return k

curve = pd.DataFrame(sse_)[1]
k = best_k(curve)
print("Best k = ", k)
