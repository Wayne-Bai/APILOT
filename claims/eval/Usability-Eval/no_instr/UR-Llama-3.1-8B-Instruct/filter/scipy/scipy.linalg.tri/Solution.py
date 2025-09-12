import numpy as np

def construct_matrix(N, M, k):
    """
    Construct (N, M) matrix filled with ones at and below the kth diagonal.

    Parameters:
    N (int): Number of rows in the matrix.
    M (int): Number of columns in the matrix.
    k (int): The kth diagonal from which to start filling with ones.

    Returns:
    np.ndarray: The constructed matrix.

    """
    # Ensure k is non-negative
    if k < 0:
        raise ValueError("k must be a non-negative integer.")

    # Initialize a matrix filled with zeros
    A = np.zeros((N, M))

    # Loop over all rows
    for i in range(N):
        # Loop over all columns
        for j in range(M):
            # Fill the matrix with ones below or at the kth diagonal
            if j <= i + k:
                A[i, j] = 1

    return A

# Example usage
N = 5
M = 7
k = 2
print(construct_matrix(N, M, k))
