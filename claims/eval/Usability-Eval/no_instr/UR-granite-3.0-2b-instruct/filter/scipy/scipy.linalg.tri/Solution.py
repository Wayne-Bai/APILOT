import numpy as np
from scipy.special import comb

def construct_matrix(N, M, k):
    # Calculate the number of elements in the kth diagonal
    num_elements = np.sum(comb(N + 1, k + 1))

    # Initialize the matrix with zeros
    A = np.zeros((N, M))

    # Fill the matrix with ones at and below the kth diagonal
    for i in range(N):
        for j in range(1, min(i + k + 1, M + 1)):
            A[i, j] = 1

    return A
