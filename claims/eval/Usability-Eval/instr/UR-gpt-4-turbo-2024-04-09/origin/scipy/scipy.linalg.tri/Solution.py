import numpy as np
from scipy.linalg import toeplitz

def ones_below_k_diagonal(N, M, k):
    # Generate the first column and first row of the matrix
    # All elements in the first column are ones since the main diagonal and below are ones
    first_col = np.ones(N)
    # For the first row, we need to determine where the ones stop
    # Ones appear until the (k+1)th element, then zeros
    first_row = np.zeros(M)
    first_row[:min(M, k+1)] = 1
    
    # Create a Toeplitz matrix using the first column and first row
    return toeplitz(first_col, first_row)

# For example, a 5x5 matrix with ones at and below the 2nd diagonal
print(ones_below_k_diagonal(5, 5, 2))
