import numpy as np
from scipy.cluster.vq import kmeans2

# Example data (replace this with your actual data)
observations = np.array([
    [1, 2], [1, 4], [1, 0], [4, 2], [4, 4], [4, 0]
])

# Number of clusters
k = 2

centers, labels = kmeans2(observations, k)
print("Clusters Centers:", centers)
print("Labels:", labels)
