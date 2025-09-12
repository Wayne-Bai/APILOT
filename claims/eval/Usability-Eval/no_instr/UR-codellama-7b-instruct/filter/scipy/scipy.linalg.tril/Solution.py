
import numpy as np
from scipy.sparse import lil_matrix

def zero_diagonal(A, k):
    n = A.shape[0]
    if k >= n:
        raise ValueError("k must be less than the number of rows in the matrix")
    new_data = np.zeros((n-k, n))
    for i in range(k):
        for j in range(i+1, n-i):
            new_data[i+j] = A[i][j+i]
    return lil_matrix((new_data, (0, n-1)))
