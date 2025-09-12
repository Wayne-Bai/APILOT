
import numpy as np
from scipy.sparse.linalg import spsolve

# Define the sparse matrix A and the vector/matrix b
A = np.array([[1, 0, 0], [0, 2, 0], [0, 0, 3]])
b_vector = np.array([1, 2, 3])

# Solve the sparse linear system Ax = b
x = spsolve(A, b_vector)

print("Solution x for vector b:", x)

# If b is a matrix
b_matrix = np.array([[1, 2], [3, 4], [5, 6]])
x_matrix = spsolve(A, b_matrix)

print("\nSolution x for matrix b:\n", x_matrix)
