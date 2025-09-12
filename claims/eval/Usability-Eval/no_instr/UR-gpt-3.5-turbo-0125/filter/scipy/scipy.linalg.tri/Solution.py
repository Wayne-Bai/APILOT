
import numpy as np

def create_diagonal_matrix(N, M, k):
    A = np.zeros((N, M))
    for i in range(N):
        for j in range(i+k+1):
            if j < M:
                A[i, j] = 1
    return A

N = 5
M = 5
k = 2
result = create_diagonal_matrix(N, M, k)
print(result)
