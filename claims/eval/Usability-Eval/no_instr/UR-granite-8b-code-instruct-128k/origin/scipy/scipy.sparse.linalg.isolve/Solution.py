import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import spsolve
# Create a sparse matrix
A = csr_matrix([[1, 2, 0], [3, 4, 5], [0, 6, 7]])
# Create a sparse vector
b = np.array([8, 9, 10])
# Solve the sparse linear system Ax=b
x = spsolve(A, b)
print(x)
