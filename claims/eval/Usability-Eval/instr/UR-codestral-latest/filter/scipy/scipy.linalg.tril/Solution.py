import numpy as np

def zero_above_kth_diag(matrix, k):
    # Create a copy of the matrix
    result = np.copy(matrix)

    # Set all elements above kth diagonal to zero
    result[np.triu_indices_from(result, k=k+1)] = 0

    return result
