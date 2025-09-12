
import numpy as np
from scipy.linalg import svd, pinv

def moore_penrose_pseudo_inverse(matrix):
    """
    Compute the (Moore-Penrose) pseudo-inverse of a Hermitian matrix.

    Parameters
    ----------
    matrix : ndarray
        A Hermitian matrix for which the pseudo-inverse is desired.

    Returns
    -------
    pinv_matrix : ndarray
        The Moore-Penrose pseudo-inverse of the input matrix.
    """
    u, sigma, vh = svd(matrix)
    inv_sigma = np.zeros_like(sigma)
    nonzero_inds = (np.abs(sigma) > 1e-15)
    inv_sigma[nonzero_inds] = 1 / sigma[nonzero_inds]
    pinv_matrix = vh.T @ np.diag(inv_sigma) @ u.T
    return pinv_matrix
