
import numpy as np
from scipy.sparse import csr_matrix, lil_matrix

def laplacian(A):
    """
    Compute the Laplacian matrix of a directed graph A.

    The Laplacian matrix is defined as:
        L = D - A
    where D is the degree matrix and A is the adjacency matrix.

    Parameters
    ----------
    A : array_like, shape (n_vertices, n_vertices)
        The directed graph represented as an adjacency matrix.

    Returns
    -------
    L : ndarray, shape (n_vertices, n_vertices)
        The Laplacian matrix of the directed graph.
    """
    # Compute the degree matrix
    D = np.diag(np.sum(A, axis=1))

    # Compute the Laplacian matrix
    L = D - A

    return L
