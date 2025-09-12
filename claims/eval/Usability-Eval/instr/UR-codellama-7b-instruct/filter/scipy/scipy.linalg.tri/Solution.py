import numpy as np
from scipy import linalg

def generate_ones_matrix(N, M, k):
    # Initialize a (N, M) matrix filled with zeros
    A = np.zeros((N, M))
    
    # Loop over the rows of the matrix
    for i in range(N):
        # Set the values below the kth diagonal to 1
        A[i, min(M-1, i+k)] = 1
    
    return A
