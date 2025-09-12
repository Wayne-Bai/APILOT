import numpy as np
from scipy.cluster.vq import kmeans, vq

# Example data: create random observations
data = np.random.rand(100, 2)  # 100 observations with 2 features
k = 3  # Number of clusters

# Perform k-means clustering
centroids, distortion = kmeans(data, k)

# Assign each observation to the nearest centroid
cluster_labels, _ = vq(data, centroids)

# Output the results
print("Centroids:")
print(centroids)
print("Cluster Labels:")
print(cluster_labels)
