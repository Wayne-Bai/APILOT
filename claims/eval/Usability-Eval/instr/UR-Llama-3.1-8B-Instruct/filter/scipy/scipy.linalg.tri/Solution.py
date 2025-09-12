import numpy as np

def construct_matrix(N, M, k):
    """
    Construct (N, M) matrix filled with ones at and below the kth diagonal.
    
    Args:
    N (int): Number of rows in the matrix.
    M (int): Number of columns in the matrix.
    k (int): The kth diagonal.

    Returns:
    numpy.ndarray: The constructed matrix.
    """
    # Initialize an (N, M) matrix with zeros
    A = np.zeros((N, M))
    
    # Fill the matrix with ones at and below the kth diagonal
    for i in range(N):
        for j in range(M):
            if j <= i + k:
                A[i, j] = 1
    
    return A

# Example usage:
N = 5  # Number of rows
M = 5  # Number of columns
k = 2  # The kth diagonal

matrix = construct_matrix(N, M, k)
print(matrix)
