import scipy.sparse.linalg as slin
import scipy.sparse as spa
import numpy as np

# Define the sparse matrix A
A = spa.csr_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Define the vector or matrix b
b = np.array([1, 2, 3])

# Solve the sparse linear system Ax=b
x = slin.spsolve(A, b)

# Print the solution
print(x)
