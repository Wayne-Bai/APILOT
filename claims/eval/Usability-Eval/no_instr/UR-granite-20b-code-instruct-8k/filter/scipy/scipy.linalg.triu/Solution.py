import numpy as np
from scipy import zeros

def zero_below_diagonal(matrix, k):
    """Make a copy of a matrix with elements below the kth diagonal zeroed."""
    matrix_copy = matrix.copy()
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if i + j < k:
                matrix_copy[i, j] = 0
    return matrix_copy
