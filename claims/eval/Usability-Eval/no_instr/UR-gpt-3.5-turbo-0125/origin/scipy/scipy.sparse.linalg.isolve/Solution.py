
import numpy as np
from scipy.sparse import csc_matrix
from scipy.sparse.linalg import spsolve

# Define a sparse matrix A
A = csc_matrix([[3, 0, 1], [0, 2, 0], [0, 0, 4]])

# Define the vector b
b_vector = np.array([1, 2, 3])

# Solve the sparse linear system Ax = b
x_vector = spsolve(A, b_vector)
print("Solution for vector b:")
print(x_vector)

# Define a matrix B
B_matrix = np.array([[1, 0, 0], [0, 2, 0], [0, 0, 3]])

# Solve the sparse linear system Ax = B
X_matrix = spsolve(A, B_matrix)
print("\nSolution for matrix B:")
print(X_matrix)
