import numpy as np
from scipy.cluster.vq import kmeans, vq

# Generate sample data
data = np.random.rand(100, 2)  # 100 observation vectors with 2 features

# Specify the number of clusters
k = 3

# Perform k-means clustering
centroids, distortion = kmeans(data, k)

# Assign each observation vector to a cluster
clusters, _ = vq(data, centroids)

print("Centroids:\n", centroids)
print("Cluster assignments:\n", clusters)
