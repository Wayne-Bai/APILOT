# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.vq import kmeans, vq

# Create a set of observation vectors
np.random.seed(0)
observation_vectors = np.vstack((np.random.normal(0, 0.5, size=(25, 2)), 
                                 np.random.normal(1, 0.5, size=(25, 2)), 
                                 np.random.normal(2, 0.5, size=(25, 2))))

# Define the number of clusters
k = 3

# Perform k-means clustering
centroids, _ = kmeans(observation_vectors, k)
idx, _ = vq(observation_vectors, centroids)

# Plot the clusters
plt.figure()
plt.scatter(observation_vectors[:, 0], observation_vectors[:, 1], c=idx)
plt.scatter(centroids[:, 0], centroids[:, 1], c='r', marker='*', s=200)
plt.show()
