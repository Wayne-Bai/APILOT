import scipy.sparse.linalg as spla
import scipy.sparse as sp
import numpy as np

# Example matrix A, which is sparse
data = np.array([1, 2, 3, 4, 5])
rows = np.array([0, 1, 2, 3, 4])
cols = np.array([0, 1, 2, 3, 4])
A = sp.csr_matrix((data, (rows, cols)), shape=(5, 5))

# Example vector b
b = np.array([1, 2, 3, 4, 5])

# Solving the linear system
x = spla.spsolve(A, b)

print("Solution of the system Ax = b:", x)
