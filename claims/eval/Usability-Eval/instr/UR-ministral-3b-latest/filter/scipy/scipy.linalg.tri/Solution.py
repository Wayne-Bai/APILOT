import numpy as np
import scipy.linalg

N = 5
M = 5
k = 3

result = np.ones((N, M), dtype=int)
for i in range(N):
    for j in range(M):
        if j <= i + k:
            result[i, j] = 1

print(result)
