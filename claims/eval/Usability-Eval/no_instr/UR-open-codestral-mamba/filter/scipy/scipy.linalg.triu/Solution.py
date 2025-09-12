import numpy as np
from scipy.sparse import csr_matrix

def zero_below_kth_diagonal(matrix, k):
    result = matrix.copy()
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if i >= j + k:
                result[i, j] = 0
    return result

# Example usage:
matrix = np.array([[1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 10,11,12],
                    [13,14,15,16]])

k = 2
zeroed_matrix = zero_below_kth_diagonal(matrix, k)
zeroed_matrix
