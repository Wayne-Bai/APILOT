
from sklearn.cluster import AgglomerativeClustering
from sklearn import datasets
import numpy as np

# Load the iris dataset
iris = datasets.load_iris()
X = iris.data[:, :2]  # we only take the first two features.

# Create an AgglomerativeClustering object and set the linkage distance
clustering = AgglomerativeClustering(n_clusters=3, affinity='euclidean', linkage='ward')

# Fit the clustering algorithm to the data
clustering.fit(X)

# Get the cluster labels for each sample
labels = clustering.labels_

# Print the cluster centroids and the number of samples in each cluster
print("Cluster centroids:")
print(clustering.cluster_centers_)
print("\nNumber of samples in each cluster:")
print(np.bincount(labels))
