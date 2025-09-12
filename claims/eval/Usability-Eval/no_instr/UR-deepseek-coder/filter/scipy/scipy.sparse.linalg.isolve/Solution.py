import scipy.sparse.linalg as spla
import scipy.sparse as sp
import numpy as np

# Example usage:
# Define a sparse matrix A and a vector/matrix b
A = sp.csr_matrix([[4, 0, 0], [0, 5, 0], [0, 0, 6]])
b = np.array([1, 2, 3])

# Solve the sparse linear system Ax = b
x = spla.spsolve(A, b)

print("Solution x:", x)
