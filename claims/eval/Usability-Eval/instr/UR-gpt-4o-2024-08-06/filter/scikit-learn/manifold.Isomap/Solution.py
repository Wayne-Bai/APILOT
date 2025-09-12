from sklearn.decomposition import PCA
from sklearn.neighbors import NearestNeighbors
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import shortest_path

def isomap(X, n_components=2, n_neighbors=5):
    """
    Perform Isomap Embedding on dataset X.

    Parameters:
    - X: array-like, shape (n_samples, n_features)
    - n_components: integer, the number of dimensions in which to immerse the data
    - n_neighbors: integer, the number of neighbors to consider for each point

    Outputs:
    - X_transformed: array-like, shape (n_samples, n_components)
    """
    # Step 1: Find the nearest neighbors
    neighbors = NearestNeighbors(n_neighbors=n_neighbors)
    neighbors.fit(X)
    distances, indices = neighbors.kneighbors(X)

    # Step 2: Construct the neighborhood graph
    n_samples = X.shape[0]
    graph = csr_matrix((n_samples, n_samples))
    for i in range(n_samples):
        for j in range(1, n_neighbors):  # start from 1 to skip self-loop
            graph[i, indices[i, j]] = distances[i, j]
            graph[indices[i, j], i] = distances[i, j]  # ensure symmetry

    # Step 3: Compute shortest paths
    geodesic_distances = shortest_path(csgraph=graph, directed=False)

    # Step 4: Centering the distance matrix
    n = geodesic_distances.shape[0]
    H = np.eye(n) - np.ones((n, n)) / n
    K = -0.5 * np.dot(H, np.dot(geodesic_distances ** 2, H))

    # Step 5: Perform eigenvalue decomposition
    eigvals, eigvecs = np.linalg.eigh(K)

    # Sort eigenvectors and eigenvalues in descending order
    idx = np.argsort(eigvals)[::-1]
    eigvals = eigvals[idx]
    eigvecs = eigvecs[:, idx]

    # Step 6: Select the top n_components eigenvectors
    X_transformed = eigvecs[:, :n_components] * np.sqrt(eigvals[:n_components])

    return X_transformed

# Example usage:
# Assuming X is your input data
# transformed_data = isomap(X, n_components=2, n_neighbors=5)
