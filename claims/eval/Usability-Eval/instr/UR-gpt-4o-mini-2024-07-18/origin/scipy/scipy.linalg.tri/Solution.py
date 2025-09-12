import numpy as np

def construct_matrix(N, M, k):
    A = np.zeros((N, M), dtype=int)
    for i in range(N):
        for j in range(M):
            if j <= i + k:
                A[i, j] = 1
    return A

# Example usage
N = 5
M = 5
k = 1
matrix = construct_matrix(N, M, k)
print(matrix)
