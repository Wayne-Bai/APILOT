import numpy as np
from scipy.linalg import toeplitz

def construct_matrix(N, M, k):
    # Create a column vector with ones at and below the kth diagonal
    col = np.zeros(N)
    col[:k+1] = 1
    
    # Create a row vector with ones at and below the kth diagonal
    row = np.zeros(M)
    row[:k+1] = 1
    
    # Construct the matrix using toeplitz function
    matrix = toeplitz(col, row)
    
    return matrix

# Example usage:
N = 5
M = 5
k = 2
result_matrix = construct_matrix(N, M, k)
print(result_matrix)
