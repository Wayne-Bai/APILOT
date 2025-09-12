import numpy as np
from scipy.sparse import csr_matrix

def laplacian_matrix(adj_matrix):
    """
    Calculate the Laplacian matrix of a directed graph.

    Parameters:
    adj_matrix (numpy.ndarray): Adjacency matrix of the directed graph.

    Returns:
    numpy.ndarray: Laplacian matrix of the directed graph.
    """
    # Calculate the degree matrix
    degree_matrix = np.diag(np.sum(adj_matrix, axis=1))

    # Calculate the Laplacian matrix
    laplacian_matrix = degree_matrix - adj_matrix

    return laplacian_matrix
