from scipy.sparse import csc_matrix
from scipy.sparse.linalg import spsolve
import numpy as np

# Create a sample sparse matrix A in compressed sparse column (CSC) format
A = csc_matrix([[3, 2, 0], [0, -1, 1], [0, 0, 5]])

# Create a vector b
b = np.array([5, -2, 10])

# Solve the sparse linear system Ax = b
x = spsolve(A, b)

# Output the solution
print("Solution vector x:", x)
