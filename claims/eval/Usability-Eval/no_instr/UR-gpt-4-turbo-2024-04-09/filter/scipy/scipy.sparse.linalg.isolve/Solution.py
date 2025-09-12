import scipy.sparse.linalg as splinalg
import scipy.sparse as sparse
import numpy as np

# Example matrix A and vector b
data = np.array([1, 2, 3, 4, 5, 6])
row_indices = np.array([0, 0, 1, 1, 2, 2])
col_indices = np.array([0, 2, 1, 2, 0, 1])
A = sparse.csr_matrix((data, (row_indices, col_indices)), shape=(3, 3))

b = np.array([1, 2, 3])

# Solve Ax = b
x = splinalg.spsolve(A, b)

print("Solution x:", x)
