from scipy.sparse import csr_matrix
from scipy.sparse.linalg import spsolve
import numpy as np

# Use CSR (Compressed Sparse Row) matrix for efficient memory usage
A = csr_matrix([[1, 0, 2], [0, 0, 0], [3, 0, 4]])

# Assume we have a vector b
b = np.array([10, 15, 20])

# Solve the sparse linear system Ax = b using spsolve
x = spsolve(A, b)

# Print the solution
print('Result: ', x)
