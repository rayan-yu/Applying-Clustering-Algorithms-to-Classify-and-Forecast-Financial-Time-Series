import numpy as np
import random
from sklearn.metrics.pairwise import pairwise_distances
#####################################################
# found this kmedoid function from 
# https://github.com/letiantian/kmedoids
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
    
    ###### ???
    #seed = 10 # random seed set so that random generator will result in deterministic results
    #np.random.seed(seed)
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
    ###### ???
    #seed = 10 # random seed set so that random generator will result in deterministic results
    #np.random.seed(seed)
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


# demo
#data2 = np.array([[1,2,3,4,2,2,2], [3,2,3,4,5,6,3],[6,8,8,7,4,8,9],[8,6,9,8,5,4,8]])
X = np.array([[1,1,1,2], [5,4,5,6], [2,1,1,2], [6,7,6,4],[8,10,9,8], [10,8,9,8], [1,2,3,2], [3,1,2,1], [9,10,7,9], [9,9,7,7]])
D2 = pairwise_distances(X, metric='euclidean')

# split into 2 clusters
M2, C2 = kMedoids(D2, 2)

print('number of medoids:', M2.size)
for point_idx in M2:
    print("data[", point_idx, "]: ", X[point_idx] )

print('clustering result:')
for label in C2:
    for point_idx in C2[label]:
        print('cluster {0}: {1}'.format(label, X[point_idx]))
            
for label in C2:
    t=[]
    center=''
    for point_idx in C2[label]:
        t = np.append(t, X[point_idx])
        if point_idx in M2:
            center = X[point_idx]
    print('cluster [{0}]: center: {1}: {2}'.format(label, center, t))
    
print("---------")
for label in C2:
    print('cluster[{0}]: data_row[{1}]={2}'.format(label, M2[label], X[M2[label]]))
    
    for point_idx in C2[label]:
        print('>>> data_row[{0}]={1}'.format(point_idx, X[point_idx]), end='')
        print(', dist[{0}, {1}]={2}'.format(M2[label], point_idx, D2[M2[label], point_idx]), end='')
        print(', dist[{0}, {1}]={2}'.format(point_idx, M2[label], D2[point_idx, M2[label]]))
        
for label in C2:
    print("cluster ----------", label, "----------")
    c_dist = []
    for point_idx in C2[label]:
        print("index ", point_idx, ": ", D2[M2[label], point_idx])
        c_dist.append((point_idx, D2[M2[label], point_idx]))
    print(c_dist)
    adist = np.array(c_dist, dtype=[('ind', int), ('dist', float)])
    print(type(adist))
    print("before sort: ", adist)
    adist.sort(order='dist')
    print("after sort: ", adist)
    sorted_ind = adist['ind']
    print("sorted index: ", sorted_ind)
    top_ten = 10 if sorted_ind.size > 10 else sorted_ind.size
    print("top ten: ", end='')
    for s_idx in range(top_ten):
        print(sorted_ind[s_idx], ", ", end='')
    print("\n")
    
# si = the average distance between each point of cluster  and the centroid of that cluster – also know as cluster diameter.
# dij = the distance between cluster centroids i and j
# Rij = (si + sj) / dij
# DB = (sum(max(Rij)) i from 1 to k) /k, i<>j

def avg_intra_cluster_dist(c_idx, C, D): # c_idx is the centroid's index, C is the array of data points indices in the cluster
    S = np.sum(D[c_idx][C])/len(C)
    return S

def cal_DB(M2, C2, D2):
    s_max_R_ij=0
    for i in range(len(M2)): # for each centroid or cluster i
        max_R_ij = 0
        s_i = avg_intra_cluster_dist(M2[i], C2[i], D2)
        for j in range(len(M2)): # another cluster j
            if i != j: # different clusters
                center_i = M2[i]
                center_j = M2[j]
                d_ij = D2[center_i][center_j]
                #print("center_i=", center_i, ", center_j=", center_j, ", d_ij=", d_ij)
                # calculate the mean intra cluster distance
                s_j = avg_intra_cluster_dist(M2[j], C2[j], D2)
                #print("got si, sj: ", s_i, s_j)
                R_ij = (s_i + s_j)/d_ij
                max_R_ij = np.maximum(R_ij, max_R_ij)
        print("adding...", max_R_ij)
        s_max_R_ij = s_max_R_ij + max_R_ij
        
    DB = s_max_R_ij/len(M2)
    print("DB = ", DB)
    return DB