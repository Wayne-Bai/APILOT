import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import normalize
from scipy.sparse.csgraph import laplacian
from scipy.sparse import csr_matrix

# Example adjacency matrix (replace with your own data)
adjacency_matrix = np.array([
    [0, 1, 0, 1],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 1, 0]
])

# Convert adjacency matrix to a sparse matrix
sparse_adjacency_matrix = csr_matrix(adjacency_matrix)

# Compute the normalized Laplacian
laplacian_matrix = laplacian(sparse_adjacency_matrix, normed=True)

# Perform eigendecomposition to get the projection
eigenvalues, eigenvectors = np.linalg.eigh(laplacian_matrix.toarray())

# Normalize the eigenvectors
normalized_eigenvectors = normalize(eigenvectors, axis=1)

# Apply clustering (e.g., KMeans) to the normalized eigenvectors
n_clusters = 2  # Number of clusters
kmeans = KMeans(n_clusters=n_clusters)
cluster_labels = kmeans.fit_predict(normalized_eigenvectors)

print("Cluster labels:", cluster_labels)
