import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import spsolve

def laplacian_of_graph(adjacency_matrix):
    """
    Calculate the Laplacian of a directed graph.

    Parameters:
    adjacency_matrix (csr_matrix): A sparse matrix representing the adjacency matrix of the graph.

    Returns:
    csr_matrix: The Laplacian matrix of the graph.
    """
    # Calculate the degree matrix
    degree_matrix = np.diag(np.sum(adjacency_matrix, axis=1))

    # Calculate the Laplacian matrix
    laplacian_matrix = degree_matrix - adjacency_matrix

    return laplacian_matrix
