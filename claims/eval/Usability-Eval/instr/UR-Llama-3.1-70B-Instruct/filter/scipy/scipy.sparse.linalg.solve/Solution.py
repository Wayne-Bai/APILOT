import scipy
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import spsolve

# Define the sparse matrix A
A = csr_matrix(np.array([[3, 0, 0], [0, 2, 0], [0, 0, 1]]))

# Define the vector or matrix b
b_vector = np.array([9, 8, 7])
b_matrix = np.array([[9, 10], [8, 9], [7, 6]])

# Solve the sparse linear system Ax = b for a vector b
x_vector = spsolve(A, b_vector)
print("Solution for vector b: ", x_vector)

# Solve the sparse linear system Ax = b for a matrix b
x_matrix = spsolve(A, b_matrix)
print("Solution for matrix b: \n", x_matrix)
