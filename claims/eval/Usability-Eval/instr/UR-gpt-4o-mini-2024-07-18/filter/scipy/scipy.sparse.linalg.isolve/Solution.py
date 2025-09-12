import numpy as np
from scipy.sparse import csc_matrix
from scipy.sparse.linalg import lsqr

# Example sparse matrix A (in Compressed Sparse Column format) and vector/matrix b
A = csc_matrix([[3, 2, 0], [0, 0, 1], [1, 0, 0]])
b = np.array([5, 1, 2])

# Solve the sparse linear system Ax = b
x = lsqr(A, b)[0]

print("Solution x:", x)
