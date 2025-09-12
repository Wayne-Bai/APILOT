import numpy as np
from scipy.cluster.vq import kmeans, vq

# Sample data
data = np.array([[1.9, 2.3], [1.5, 2.5], [0.8, 0.6], [0.4, 1.8], [0.8, 0.6],
                 [0.4, 1.8], [1.9, 2.3], [1.5, 2.5], [0.8, 0.6], [0.4, 1.8]])

# Number of clusters
k = 2

# Perform k-means clustering
centroids, distortion = kmeans(data, k)

# Assign each sample to a cluster
cluster_indices, _ = vq(data, centroids)

print("Centroids:\n", centroids)
print("Cluster Indices:\n", cluster_indices)
