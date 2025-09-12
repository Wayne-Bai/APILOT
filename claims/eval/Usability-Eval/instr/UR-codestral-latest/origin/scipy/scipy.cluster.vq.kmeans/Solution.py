# Import the necessary libraries
from scipy.cluster.vq import kmeans
import numpy as np

# Define the observation vectors as a 2D numpy array
observations = np.array([[1, 2], [2, 3], [8, 9], [9, 10]])

# Define the number of clusters to form
k = 2

# Use the kmeans function from scipy.cluster.vq to compute k clusters
centroids, label = kmeans(observations, k)

# Print the centroids of the k clusters
print(centroids)
