import numpy as np
from scipy.linalg import isupper

def zero_kth_diagonal(matrix, k):
    # Check if the matrix is square and has the specified kth diagonal
    if not matrix.transpose() == matrix:
        raise ValueError("The matrix must be square.")

    # Create a copy of the matrix
    copied_matrix = matrix.copy()

    # Iterate over the matrix and set elements of the kth diagonal below the kth row to zero
    for i in range(k, matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if j >= i:
                if isupper(matrix[i, j]):
                    copied_matrix[i, j] = 0

    return copied_matrix

# Example usage:
matrix = np.array([[1, 2, 3], [4, 0, 6], [7, 8, 9]])
k = 1
result = zero_kth_diagonal(matrix, k)
print(result)
