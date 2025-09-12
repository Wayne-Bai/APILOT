import scipy.sparse.linalg as spla
import scipy.sparse as sps
import numpy as np

# Example sparse matrix A and vector/matrix b
A = sps.csr_matrix([[4, 0, 0], [0, 5, 0], [0, 0, 6]])
b = np.array([1, 2, 3])  # or b = np.array([[1, 2], [2, 3], [3, 4]]) for a matrix

# Solve the sparse linear system Ax = b
x = spla.spsolve(A, b)

print("Solution x:", x)
