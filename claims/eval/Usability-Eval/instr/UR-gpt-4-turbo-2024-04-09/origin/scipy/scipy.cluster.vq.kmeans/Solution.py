import numpy as np
from scipy.cluster.vq import kmeans

# Sample data: Observations
data = np.array([[1, 2], [1, 4], [1, 0],
                 [10, 2], [10, 4], [10, 0]])

# Number of clusters
k = 2

# Performing k-means clustering
centroids, distortion = kmeans(data, k)

print("Centroids:\n", centroids)
print("Distortion:", distortion)
