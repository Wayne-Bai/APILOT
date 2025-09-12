import numpy as np
from scipy.sparse import diags

def construct_matrix(N, M, k):
    # Create a matrix with ones on and below the k-th diagonal
    diagonals = [[1] * (M if i == 0 else M - i) for i in range(k+1)]
    offsets = np.arange(k+1)
    matrix = diags(diagonals, offsets, shape=(N, M)).toarray()
    return matrix

# Usage example
N = 5
M = 5
k = 1
matrix = construct_matrix(N, M, k)
print(matrix)
