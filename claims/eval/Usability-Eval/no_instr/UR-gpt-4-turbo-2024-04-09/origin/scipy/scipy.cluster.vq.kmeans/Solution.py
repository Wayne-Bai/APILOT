import numpy as np
from scipy.cluster.vq import kmeans, vq

# Generate random data points
data = np.random.rand(100, 3)  # 100 observations and 3 features

# Number of clusters
k = 5

# Perform k-means clustering
centroids, distortion = kmeans(data, k)

# Assign each sample to a cluster
clx, _ = vq(data, centroids)

print("Centroids:\n", centroids)
print("Cluster assignments:", clx)
