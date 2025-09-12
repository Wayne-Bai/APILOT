import numpy as np
from scipy.cluster.vq import kmeans, vq

# Example observation vectors (replace with your data)
observations = np.array([[1.0, 2.0], [1.5, 1.8], [5.0, 8.0], [8.0, 8.0], [1.0, 0.6], [9.0, 11.0]])

# Number of clusters
k = 2

# Perform k-means clustering
centroids, distortion = kmeans(observations, k)

# Assign each observation to a cluster
cluster_indices, _ = vq(observations, centroids)

print("Centroids:", centroids)
print("Cluster Indices:", cluster_indices)
