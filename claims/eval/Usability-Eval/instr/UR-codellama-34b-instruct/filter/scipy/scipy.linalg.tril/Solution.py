
import numpy as np
from scipy.linalg import toeplitz

def zero_above_diagonal(matrix, k):
    """
    Return a copy of the input matrix with elements above the kth diagonal zeroed.

    Parameters
    ----------
    matrix : ndarray
        The input matrix.
    k : int
        The diagonal index to zero elements above.

    Returns
    -------
    out : ndarray
        A copy of the input matrix with elements above the kth diagonal zeroed.
    """
    # Create a toeplitz matrix from the input matrix
    toeplitz_matrix = toeplitz(matrix)

    # Zero elements above the kth diagonal
    zero_mask = np.zeros_like(toeplitz_matrix, dtype=bool)
    zero_mask[np.triu_indices(toeplitz_matrix.shape[0], k=k)] = True
    toeplitz_matrix[zero_mask] = 0

    # Return the zeroed toeplitz matrix
    return toeplitz_matrix
