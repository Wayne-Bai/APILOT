import numpy as np

def zero_below_diag(matrix, k):
    # Create a copy of the matrix
    result = np.copy(matrix)

    # Set elements below the kth diagonal to zero
    result[np.tril_indices(result.shape[0], -1, k)] = 0

    return result
