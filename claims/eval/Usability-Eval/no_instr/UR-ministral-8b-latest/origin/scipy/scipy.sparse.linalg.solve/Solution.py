import scipy.sparse as sp
import numpy as np

# Example sparse matrix and vector
A = sp.csr_matrix([[3, 0, 1], [0, 4, 1], [4, 1, 2]])
b = np.array([3, 2, 1])

# Solving the sparse linear system Ax=b
x = sp.linalg.spsolve(A, b)

print("Solution:", x)
