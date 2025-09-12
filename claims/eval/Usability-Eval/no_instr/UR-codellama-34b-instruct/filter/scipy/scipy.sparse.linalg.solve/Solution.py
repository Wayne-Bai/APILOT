import numpy as np
from scipy.sparse import csc_matrix, lil_matrix
from scipy.sparse.linalg import spsolve

# Define the matrix A and the vector b
A = csc_matrix([[1, 0], [0, 2]])
b = np.array([1, 2])

# Convert A to a sparse matrix if it's not already one
if not isinstance(A, spsparse):
    A = csc_matrix(A)

# Solve the linear system Ax = b using spsolve()
x = spsolve(A, b)

# Print the solution
print(x)
