import numpy as np
from scipy.linalg import solve_triangular

def zero_below_kth_diagonal(A, k):
    n = A.shape[0]
    B = np.zeros((n, n))
    for i in range(n):
        for j in range(i+1, n):
            if i < k:
                B[j, i] = 0
    return B
