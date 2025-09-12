from scipy.cluster.vq import kmeans, vq
import numpy as np

# Generate some random observation vectors
obs = np.random.rand(100, 2)

# Perform k-means clustering
centroids, distortion = kmeans(obs, 5)

# Assign each observation vector to a cluster
_,_, assigned = vq(obs, centroids)
