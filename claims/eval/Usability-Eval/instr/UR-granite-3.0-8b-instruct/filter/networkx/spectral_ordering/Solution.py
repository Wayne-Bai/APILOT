import networkx as nx
import numpy as np

def spectral_ordering(G):
    # Compute the Laplacian matrix of the graph
    L = nx.laplacian_matrix(G).toarray()

    # Compute the eigenvalues and eigenvectors of the Laplacian matrix
    eigenvalues, eigenvectors = np.linalg.eig(L)

    # Find the index of the second smallest eigenvalue (Fiedler vector)
    fiedler_index = np.argsort(eigenvalues)[1]

    # Compute the spectral ordering of the nodes
    spectral_order = np.argsort(eigenvectors[:, fiedler_index])

    # Return the spectral ordering of the nodes
    return spectral_order
