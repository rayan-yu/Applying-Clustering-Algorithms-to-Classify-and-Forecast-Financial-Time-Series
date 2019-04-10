#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
from scipy import stats
import random
from sklearn.metrics.pairwise import pairwise_distances

##################################################
# code from https://github.com/letiantian/kmedoids
#
# define kMedoids function
def kMedoids(D, k, tmax=100):
    # determine dimensions of distance matrix D
    m, n = D.shape

    if k > n:
        raise Exception('too many medoids')

    # find a set of valid initial cluster medoid indices since we
    # can't seed different clusters with two points at the same location
    valid_medoid_inds = set(range(n))
    invalid_medoid_inds = set([])
    rs,cs = np.where(D==0)
    # the rows, cols must be shuffled because we will keep the first duplicate below
    index_shuf = list(range(len(rs)))
    np.random.shuffle(index_shuf)
    rs = rs[index_shuf]
    cs = cs[index_shuf]
    for r,c in zip(rs,cs):
        # if there are two points with a distance of 0...
        # keep the first one for cluster init
        if r < c and r not in invalid_medoid_inds:
            invalid_medoid_inds.add(c)
    valid_medoid_inds = list(valid_medoid_inds - invalid_medoid_inds)

    if k > len(valid_medoid_inds):
        raise Exception('too many medoids (after removing {} duplicate points)'.format(
            len(invalid_medoid_inds)))

    # randomly initialize an array of k medoid indices
    M = np.array(valid_medoid_inds)
    np.random.shuffle(M)
    M = np.sort(M[:k])

    # create a copy of the array of medoid indices
    Mnew = np.copy(M)

    # initialize a dictionary to represent clusters
    C = {}
    for t in range(tmax):
        # determine clusters, i. e. arrays of data indices
        J = np.argmin(D[:,M], axis=1)
        for kappa in range(k):
            C[kappa] = np.where(J==kappa)[0]
        # update cluster medoids
        for kappa in range(k):
            J = np.mean(D[np.ix_(C[kappa],C[kappa])],axis=1)
            j = np.argmin(J)
            Mnew[kappa] = C[kappa][j]
        np.sort(Mnew)
        # check for convergence
        if np.array_equal(M, Mnew):
            break
        M = np.copy(Mnew)
    else:
        # final update of cluster memberships
        J = np.argmin(D[:,M], axis=1)
        for kappa in range(k):
            C[kappa] = np.where(J==kappa)[0]

    # return results
    return M, C

################################################################
# Calculate KMedoid clusters
#
# split into 3 clusters by distance matrix
# M2 is an array of medoid index, C2 is a dictionary that has an array of index for each cluster# read in the stock price matrix
stock_prices_csv = 'C:/ry_sci/demo/tickerprice_demo.csv'
df = pd.read_csv(stock_prices_csv, index_col=['Symbol'], header=0)

# calculate zscore
dz = stats.zscore(df, axis=1)
dfz= pd.DataFrame(dz, index=df.index, columns=df.columns)

# calculate distance matrix
D2 = pairwise_distances(dfz, metric='euclidean')

# calculate medoid and cluster
M2, C2 = kMedoids(D2, 3)

print("number of tickers:", len(df.index))
print('number of medoids:', M2.size)

# output medoids
for point_idx in M2:
    print("cluster medoid ticker_row[", point_idx, "]: ", dfz.index[point_idx] )

# output each cluster tickers
print('\n clustering result:')
for label in C2:
    for point_idx in C2[label]:
        print('cluster {0}:　{1}'.format(label, dfz.index[point_idx]))

# output each cluster tickers
for label in C2:
    t=[]
    center=''
    for point_idx in C2[label]:
        t = np.append(t, dfz.index[point_idx])
        if point_idx in M2:
            center = dfz.index[point_idx]
        
    print('cluster [{0}]:　center: {1}: {2}'.format(label, center, t))

