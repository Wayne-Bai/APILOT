import networkx as nx
import numpy as np

def spectral_ordering(graph):
    # Compute the Laplacian matrix of the graph
    laplacian = nx.laplacian_matrix(graph)

    # Compute the eigenvalues and eigenvectors of the Laplacian matrix
    eigenvalues, eigenvectors = np.linalg.eig(laplacian.toarray())

    # Find the index of the second smallest eigenvalue (Fiedler vector)
    fiedler_index = np.argmin(eigenvalues[np.argsort(eigenvalues)[:-1]])

    # Sort the nodes by their corresponding elements in the Fiedler vector
    ordering = np.argsort(eigenvectors[:, fiedler_index])

    return ordering

# Example usage:
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 3), (4, 5), (4, 6), (5, 6)])
ordering = spectral_ordering(G)
print(ordering)
