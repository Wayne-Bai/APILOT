import scipy.sparse
import numpy as np

# Create a sparse matrix A
A = scipy.sparse.rand(5, 5, density=0.1)

# Create a vector b
b = np.ones(5)

# Solve for x
x = scipy.sparse.linalg.spsolve(A, b)
x
