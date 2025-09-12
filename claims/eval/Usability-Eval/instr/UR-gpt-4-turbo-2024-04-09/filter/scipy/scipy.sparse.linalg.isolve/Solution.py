import scipy.sparse.linalg as spla
import scipy.sparse as sp
import numpy as np

# Example sparse matrix A
data = np.array([1, 2, 3, 4, 5, 6])
row_indices = np.array([0, 0, 1, 2, 2, 3])
col_indices = np.array([0, 2, 2, 0, 1, 2])
A = sp.csr_matrix((data, (row_indices, col_indices)), shape=(4, 3))

# Example vector b
b = np.array([1, 2, 3, 4])

# Solve the sparse linear system Ax = b using scipy
x = spla.spsolve(A, b)

print("Solution x =", x)
