
import numpy as np
from scipy.linalg import toeplitz

def construct_matrix(N, M, k):
    # Construct a (N, M) matrix filled with ones at and below the kth diagonal
    diag_values = np.ones((M,), dtype=np.int64)
    diag_indices = np.arange(N - k + 1)
    offdiag_values = np.zeros((N - k, M), dtype=np.int64)
    return toeplitz(offdiag_values, diag_values[None,:], diag_indices=diag_indices)
