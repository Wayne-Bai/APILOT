import numpy as np
from scipy.sparse import csc_matrix
from scipy.sparse.linalg import spsolve

# Example inputs
A = csc_matrix([[3, 2, 0], [1, -1, 0], [0, 5, 1]]) # Sparse matrix A
b = np.array([1, 2, 3]) # Vector b

# Solving the sparse linear system Ax = b
x = spsolve(A, b)

print("Solution vector x:", x)
