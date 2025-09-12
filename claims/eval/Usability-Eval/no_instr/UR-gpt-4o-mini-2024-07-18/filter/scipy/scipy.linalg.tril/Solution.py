import numpy as np
from scipy.linalg import banded

def zero_above_kth_diagonal(matrix, k):
    # Create a copy of the original matrix
    matrix_copy = np.copy(matrix)
    
    # Get the shape of the matrix
    n, m = matrix_copy.shape
    
    # Set elements above the k-th diagonal to zero
    for i in range(n):
        for j in range(m):
            if j > i + k:  # Element is above the k-th diagonal
                matrix_copy[i, j] = 0
                
    return matrix_copy

# Example usage
matrix = np.array([[1, 2, 3], 
                   [4, 5, 6], 
                   [7, 8, 9]])

k = 1
result = zero_above_kth_diagonal(matrix, k)
print(result)
