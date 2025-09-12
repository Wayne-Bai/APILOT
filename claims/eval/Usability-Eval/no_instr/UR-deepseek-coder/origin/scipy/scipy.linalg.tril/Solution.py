import numpy as np
from scipy import linalg

def zero_above_kth_diagonal(matrix, k):
    # Create a copy of the matrix
    result = np.copy(matrix)
    
    # Zero out elements above the kth diagonal
    for i in range(result.shape[0]):
        for j in range(result.shape[1]):
            if j > i + k:
                result[i, j] = 0
    
    return result

# Example usage:
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
k = 1
result_matrix = zero_above_kth_diagonal(matrix, k)
print(result_matrix)
