# Import necessary libraries
import scipy.sparse as sp
import scipy.sparse.linalg as la
import numpy as np

# Create a sparse matrix A
A = sp.csr_matrix(np.array([[3, 0, 0], [0, 2, 0], [0, 0, 1]]))

# Create a vector b
b = np.array([6, 4, 3])

# Solve the linear system Ax = b
x = la.spsolve(A, b)

print("Solution x:", x)

# Create a matrix B
B = np.array([[6, 4], [3, 2], [1, 1]])

# Solve the linear system AX = B
X = la.spsolve(A, B)

print("Solution X:\n", X)
