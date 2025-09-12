import numpy as np
from scipy import linalg

def make_below_k_diag_zero(matrix, k):
    # Create an identity matrix of the same shape as 'matrix'
    mask = np.eye(matrix.shape[0], matrix.shape[1], k=k, dtype=bool)
    
    # Make a copy of the matrix
    result = matrix.copy()
    
    # Zero out elements below k-th diagonal
    result[~mask] = 0
    return result

# Example usage
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
k = 1
new_matrix = make_below_k_diag_zero(matrix, k)
print(new_matrix)
