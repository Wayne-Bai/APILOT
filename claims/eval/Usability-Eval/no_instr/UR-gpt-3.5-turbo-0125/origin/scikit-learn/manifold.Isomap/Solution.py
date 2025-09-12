
import numpy as np
from sklearn.utils import check_random_state
from sklearn.metrics import euclidean_distances
from sklearn.decomposition import KernelPCA
from sklearn.neighbors import NearestNeighbors
from sklearn.manifold.t_sne import trustworthiness
from sklearn.manifold.isomap import Isomap

# Define your data
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

# Define number of neighbors for Isomap
n_neighbors = 2

# Define number of components for Isomap
n_components = 2

# Create Isomap embedding
isomap_embedding = Isomap(n_neighbors=n_neighbors, n_components=n_components)
X_transformed = isomap_embedding.fit_transform(X)

print(X_transformed)
