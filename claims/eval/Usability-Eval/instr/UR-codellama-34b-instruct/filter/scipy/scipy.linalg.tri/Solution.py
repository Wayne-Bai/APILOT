
import numpy as np

def construct_matrix(N, M, k):
    # Initialize a matrix of size (N x M) with all elements set to zero
    A = np.zeros((N, M))
    
    # Loop over each row of the matrix
    for i in range(N):
        # Set the diagonal and all elements below it to one
        A[i, i:M] = 1
        
        # If the current element is below the kth diagonal, set it to zero
        if i > k:
            A[i, :k-1] = 0
    
    return A
