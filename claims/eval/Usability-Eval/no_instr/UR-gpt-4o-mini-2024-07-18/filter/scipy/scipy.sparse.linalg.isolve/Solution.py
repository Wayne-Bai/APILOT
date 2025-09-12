import numpy as np
from scipy.sparse import csc_matrix
from scipy.sparse.linalg import spsolve

# Example: Define a sparse matrix A and a vector/matrix b
A = csc_matrix([[3, 2, 0], [2, 3, 1], [0, 1, 2]])
b = np.array([5, 6, 5])  # Example with vector b

# To solve Ax = b
x = spsolve(A, b)

print("Solution x:\n", x)

# If b is a matrix
b_matrix = np.array([[5], [6], [5]])  # Example with matrix b
x_matrix = spsolve(A, b_matrix)

print("Solution x for matrix b:\n", x_matrix)
