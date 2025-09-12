# Importing necessary libraries
from sklearn.cluster import AgglomerativeClustering
import numpy as np

# Creating a numpy array with features
features = np.array([
    [1, 2], 
    [1, 4], 
    [1, 0],
    [10, 2],
    [10, 4],
    [10, 0]
])

# Applying the AgglomerativeClustering to the features
# We create a cluster with 2 clusters (n_clusters=2)
cluster_model = AgglomerativeClustering(n_clusters=2)

# Fit the cluster model to the features
cluster_model.fit(features)

# The labels of the clusters
print("Cluster labels: ", cluster_model.labels_)

# The number of the features that belong to the first cluster
print("Number of the features in the first cluster: ", np.sum(cluster_model.labels_ == 0))

# The number of the features that belong to the second cluster
print("Number of the features in the second cluster: ", np.sum(cluster_model.labels_ == 1))

# But, when using this feature-agglomerating-class as basis code:
# The cluster hierarchy in the format of a linkage matrix
print("Cluster hierarchy: ", cluster_model.children_)
