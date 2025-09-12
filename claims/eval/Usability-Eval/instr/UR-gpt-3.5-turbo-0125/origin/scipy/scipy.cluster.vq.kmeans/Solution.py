
import numpy as np
from scipy.cluster.vq import kmeans, vq

# Generating random data points for clustering
np.random.seed(0)
data_points = np.random.randn(100, 2)

# Choosing the number of clusters (k)
k = 3

# Perform k-means clustering
centroids, _ = kmeans(data_points, k)
clusters, _ = vq(data_points, centroids)

print("Cluster centroids:")
print(centroids)
print("Cluster assignments:")
print(clusters)
