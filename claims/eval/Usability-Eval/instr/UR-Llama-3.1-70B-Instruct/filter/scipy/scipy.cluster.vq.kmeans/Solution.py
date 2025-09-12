import numpy as np
from scipy.cluster.vq import kmeans2

# Generate some sample data
np.random.seed(0)
observation_vectors = np.random.multivariate_normal([0, 0], [[1, 0.5], [0.5, 1]], 100)

# Define the number of clusters
k = 3

# Perform k-means clustering
centroids, labels = kmeans2(observation_vectors, k)

# Print the centroids
print("Centroids:")
print(centroids)

# Print the labels
print("\nLabels:")
print(labels)

# Visualize the clusters
import matplotlib.pyplot as plt

plt.scatter(observation_vectors[:, 0], observation_vectors[:, 1], c=labels)
plt.scatter(centroids[:, 0], centroids[:, 1], c=np.arange(k), marker='*', s=200)
plt.show()
