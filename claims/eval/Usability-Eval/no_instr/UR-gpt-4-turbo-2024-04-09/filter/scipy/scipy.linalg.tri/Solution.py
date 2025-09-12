import numpy as np
from scipy.linalg import toeplitz

def create_matrix(N, M, k):
    # Create the first column and the first row for the Toeplitz matrix
    c = np.zeros(N)
    r = np.zeros(M)

    # Set ones as described. j <= i + k translates to getting the indices right for 1s
    max_index = min(N, M, k+1)
    c[:max_index] = 1
    r[0] = 1  # First element of first row is also 1
    
    # Generate the Toeplitz matrix
    matrix = toeplitz(c, r)
    return matrix

# Example usage: 
N, M, k = 5, 4, 2  # Dimensions of matrix and k-th diagonal
matrix = create_matrix(N, M, k)
print(matrix)
