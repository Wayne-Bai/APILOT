import numpy as np
from scipy.linalg import tril

def zero_below_kth_diagonal(matrix, k):
    # Create a copy of the matrix
    matrix_copy = np.copy(matrix)
    # Zero out elements below the kth diagonal
    matrix_copy = tril(matrix_copy, k=k-1)
    return matrix_copy

# Example usage:
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
k = 1
result = zero_below_kth_diagonal(matrix, k)
print(result)
