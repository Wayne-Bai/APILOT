import numpy as np

def zero_elements_above_kth_diagonal(matrix, k):
    n = matrix.shape[0]
    diagonal_index = np.arange(n - k, n)
    matrix[np.triu_indices(n, k=k)[0][diagonal_index], np.triu_indices(n, k=k)[1][diagonal_index]] = 0
    return matrix
