from scipy.sparse import csc_matrix
from scipy.sparse.linalg import spsolve
import numpy as np

# Create a sparse matrix A and vector b
n = 10  # size of the matrix
A = csc_matrix(np.random.rand(n, n))
b = np.random.rand(n)

# Solve the system Ax = b
x = spsolve(A, b)
