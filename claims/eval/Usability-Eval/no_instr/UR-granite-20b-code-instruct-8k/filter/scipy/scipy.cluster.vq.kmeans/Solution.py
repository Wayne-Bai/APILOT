from scipy.cluster.vq import kmeans
import numpy as np

# Generate random observation vectors
data = np.random.rand(100, 3)

# Determine the number of clusters
k = 5

# Run k-means clustering
centroids, _ = kmeans(data, k)
