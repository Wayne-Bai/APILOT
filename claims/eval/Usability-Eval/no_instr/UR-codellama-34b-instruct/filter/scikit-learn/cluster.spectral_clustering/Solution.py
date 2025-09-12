import numpy as np
from sklearn.cluster import SpectralClustering

# Generate some data
n_samples = 1000
X = np.random.rand(n_samples, 2)

# Compute the normalized Laplacian
L = np.linalg.norm(np.random.rand(n_samples, n_samples), axis=1)
L = L / L.max()

# Perform clustering on the projection of the normalized Laplacian
clusters = SpectralClustering(n_clusters=2).fit(X.dot(L))
