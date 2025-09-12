import scipy.cluster.vq as vq
import numpy as np

# Assuming we have two clusters and 100 observation vectors with 5 features
k = 2
observation_vectors = np.random.rand(100, 5)

# Perform k-means clustering
centroids, _ = vq.kmeans(observation_vectors, k)

# Now 'centroids' contains the final centroids of our k clusters
