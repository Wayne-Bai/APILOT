import numpy as np
from scipy.sparse import csr_matrix

def zero_above_kth_diagonal(matrix, k):
    # Convert the matrix to a sparse matrix for efficient diagonal access
    sparse_matrix = csr_matrix(matrix)

    # Create a new sparse matrix with the same shape as the original
    zero_matrix = csr_matrix(matrix.shape)

    # Iterate over the kth diagonal and above
    for i in range(k, sparse_matrix.shape[0]):
        for j in range(k, sparse_matrix.shape[1]):
            if sparse_matrix[i, j] != 0:
                zero_matrix[i, j] = 0

    return zero_matrix.toarray()
