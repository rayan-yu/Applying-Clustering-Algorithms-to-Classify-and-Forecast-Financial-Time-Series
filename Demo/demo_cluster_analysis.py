from sklearn import metrics
from sklearn.metrics import pairwise_distances
from sklearn import datasets
import numpy as np

dataset = datasets.load_iris()
X = dataset.data
y = dataset.target

##########################
# calinski_harabaz_score
from sklearn.cluster import KMeans
kmeans_model = KMeans(n_clusters=3, random_state=1).fit(X)
labels = kmeans_model.labels_
metrics.calinski_harabaz_score(X, labels)  

##########################
# davies_bouldin_score: this function needs sklearn 0.20.0
# Zero is the lowest possible score. Values closer to zero indicate a better partition.
# check sklearn version
import sklearn
print(sklearn.__version__)

# update conda to latest sklearn
# anaconda is currently 0.19.2
# open anaconda console, type in: conda install scikit-learn=0.20.0

from sklearn.metrics import davies_bouldin_score
kmeans = KMeans(n_clusters=3, random_state=1).fit(X)
labels = kmeans.labels_
davies_bouldin_score(X, labels)  
