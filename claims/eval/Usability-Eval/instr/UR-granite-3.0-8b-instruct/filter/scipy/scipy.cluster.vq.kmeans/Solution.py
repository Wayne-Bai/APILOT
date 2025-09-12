from scipy.cluster.vq import kmeans, vq
import numpy as np

# Generate some random observation vectors
obs = np.random.rand(100, 2)

# Perform k-means clustering
centroids, distortion = kmeans(obs, 3)

# Assign each observation vector to a cluster
codebook, distortion = vq(obs, centroids)
