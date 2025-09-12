import numpy as np

def construct_ones_matrix(N, M, k):
    """Construct (N, M) matrix filled with ones at and below the kth diagonal.

    Args:
    N (int): Number of rows in the matrix.
    M (int): Number of columns in the matrix.
    k (int): The kth diagonal below which entries should be 1.

    Returns:
    numpy.ndarray: A (N, M) matrix filled with ones at and below the kth diagonal.
    """
    A = np.zeros((N, M))
    for i in range(N):
        for j in range(M):
            if j <= i + k:
                A[i, j] = 1
    return A
