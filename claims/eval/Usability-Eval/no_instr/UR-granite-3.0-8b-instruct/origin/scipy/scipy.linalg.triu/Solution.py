import numpy as np
from scipy.linalg import block_diag

def zero_below_kth_diagonal(matrix, k):
    n = matrix.shape[0]
    diag = np.eye(n, k=k)
    zeros = np.zeros((n, n-k))
    return block_diag(matrix, zeros) + diag
