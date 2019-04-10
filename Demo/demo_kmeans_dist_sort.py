import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin_min
#X = np.random.randn(10, 4) # generate a 10 row, 4 column random number matrix
X = np.array([[1,1,1,2], [5,4,5,6], [2,1,1,2], [6,7,6,4],[8,10,9,8], [10,8,9,8], [1,2,3,2], [3,1,2,1], [9,10,7,9], [9,9,7,7]])
# clustering
print("X is: \n", X)

km = KMeans(n_clusters=3).fit(X) # create 3 clusters
closest, _ = pairwise_distances_argmin_min(km.cluster_centers_, X)
closest  # gives out the closest data point to the center points, an array, the first is the closest to the first cluster center, the second to the second cluster, etc.
print("closest to each cluster: ", closest)

# sort and output the closest data points
km.cluster_centers_ # the center points
centers = np.array(km.cluster_centers_)
num_closest = 4 # number of closest points to cluster center
num_clusters = 3

print("\n...clustering into 3 clusters...")
dist = km.transform(X)
print("distance matrix: \n", dist)
print("\n")
for i in range(0, num_clusters):
    print("cluster ", i, ", center: ", centers[i])
    d = dist[:, i]
    print("d to cluster center", i, ":", d)
    ind = np.argsort(d)[::][:num_closest] # an array of indices that are sorted by distance to the cluster center
    print("top closest index ", ind)
    print("top closest datapoints \n", X[ind])  # X[ind][0] is the closest, X[ind][1] is the second,  etc.
    print("----\n")
    