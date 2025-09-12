
import numpy as np
from scipy.linalg import block_diag

def zero_above_kth_diag(matrix, k):
    # Get the shape of the matrix
    num_rows, num_cols = matrix.shape

    # Create a zero matrix with the same shape as the input matrix
    result = np.zeros((num_rows, num_cols))

    # Copy the elements below the kth diagonal from the input matrix to the result matrix
    for i in range(k):
        for j in range(i + 1, min(num_rows - i, num_cols - i)):
            result[i][j] = matrix[i][j]

    return result
