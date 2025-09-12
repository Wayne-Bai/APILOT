
import numpy as np

def create_matrix(N, M, k):
    A = np.zeros((N, M))
    for i in range(N):
        for j in range(min(M, i + k + 1)):
            A[i, j] = 1
    return A

N, M, k = 5, 5, 2
result_matrix = create_matrix(N, M, k)
print(result_matrix)
