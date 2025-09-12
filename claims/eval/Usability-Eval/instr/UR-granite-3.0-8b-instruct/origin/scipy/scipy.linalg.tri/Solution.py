import numpy as np

def construct_matrix(N, M, k):
    matrix = np.ones((N, M))
    for i in range(N):
        for j in range(min(i + k + 1, M)):
            matrix[i, j] = 0
    return matrix
