import networkx as nx
import numpy as np

# Create a graph
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 5), (3, 4), (3, 6), (4, 7), (5, 7), (6, 7)])

# Compute the Laplacian matrix
L = nx.laplacian_matrix(G)

# Compute the Fiedler vector
eigenvalues, eigenvectors = np.linalg.eig(L.toarray())
fiedler_vector = eigenvectors[:, np.argsort(eigenvalues)[-2]]

# Compute the spectral ordering
spectral_ordering = np.argsort(eigenvalues)[np.argsort(np.abs(fiedler_vector))]

print(spectral_ordering)
