from sklearn.cluster import KMeans
from sklearn.preprocessing import normalize
from sklearn.manifold import SpectralEmbedding
from sklearn.neighbors import kneighbors_graph
import numpy as np

# Sample adjacency matrix for a graph
adjacency_matrix = np.array([
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [0, 1, 1, 0]
])

# Create the Laplacian matrix
laplacian_matrix = np.diag(adjacency_matrix.sum(axis=1)) - adjacency_matrix

# Normalize the Laplacian matrix
normalized_laplacian = normalize(laplacian_matrix, norm='l1')

# Apply Spectral Embedding (which is essentially a projection using the normalized Laplacian)
embedding = SpectralEmbedding(n_components=2, affinity='precomputed')
laplacian_projection = embedding.fit_transform(normalized_laplacian)

# Perform KMeans clustering on the projected data
kmeans = KMeans(n_clusters=2, random_state=42)
clusters = kmeans.fit_predict(laplacian_projection)

print("Cluster labels for the nodes:", clusters)
