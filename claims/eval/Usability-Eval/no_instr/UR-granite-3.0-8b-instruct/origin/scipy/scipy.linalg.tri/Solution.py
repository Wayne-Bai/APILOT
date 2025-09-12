import numpy as np

def generate_matrix(N, M, k):
    matrix = np.ones((N, M))
    for i in range(N):
        matrix[i, i + k:] = 0
    return matrix
