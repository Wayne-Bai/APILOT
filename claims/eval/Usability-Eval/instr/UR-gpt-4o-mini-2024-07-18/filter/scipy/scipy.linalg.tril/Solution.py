import numpy as np
from scipy.linalg import tril

def zero_above_kth_diagonal(matrix, k):
    # Create a copy of the matrix
    matrix_copy = np.copy(matrix)
    # Zero out elements above the kth diagonal
    matrix_copy = tril(matrix_copy, k)
    return matrix_copy

# Example usage
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

k = 1
result = zero_above_kth_diagonal(matrix, k)
print(result)
