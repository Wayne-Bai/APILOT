import numpy as np

def construct_matrix(N, M, k):
    matrix = np.zeros((N, M))
    for i in range(N):
        for j in range(M):
            if j <= i + k:
                matrix[i, j] = 1
    return matrix

N = 5
M = 10
k = 3
matrix = construct_matrix(N, M, k)
print(matrix)
