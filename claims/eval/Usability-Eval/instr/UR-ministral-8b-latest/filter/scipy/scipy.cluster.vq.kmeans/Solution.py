import numpy as np
from scipy.sparse import csr_matrix
from scipy.cluster.vq import kmeans

# Generating some sample data
data = np.array([[1, 2], [1, 4], [1, 0], [10, 2], [10, 4], [10, 0]])

# Perform k-means clustering
centroids, _ = kmeans(data, 2)

print("Centroids:\n", centroids)
