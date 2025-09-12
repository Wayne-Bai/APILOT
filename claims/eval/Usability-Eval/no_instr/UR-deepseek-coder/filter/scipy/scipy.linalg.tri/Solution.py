import numpy as np
from scipy.linalg import toeplitz

def construct_matrix(N, M, k):
    # Create a vector for the first row of the Toeplitz matrix
    first_row = np.zeros(M)
    first_row[:k+1] = 1
    
    # Create a vector for the first column of the Toeplitz matrix
    first_col = np.zeros(N)
    first_col[0] = 1
    
    # Construct the Toeplitz matrix
    matrix = toeplitz(first_col, first_row)
    
    return matrix

# Example usage:
N = 5
M = 5
k = 2
result = construct_matrix(N, M, k)
print(result)
