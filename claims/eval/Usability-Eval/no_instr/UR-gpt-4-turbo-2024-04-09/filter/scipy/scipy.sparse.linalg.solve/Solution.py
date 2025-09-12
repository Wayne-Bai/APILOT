import scipy.sparse.linalg as spla
import scipy.sparse as sp
import numpy as np

# Create an example sparse matrix A and a right-hand side vector b
size = 1000  # Define the size of the matrix
A = sp.rand(size, size, density=0.01, format='csr')  # Create a sparse matrix in CSR format
b = np.random.rand(size)  # Create a random vector b

# Solve the sparse linear system Ax = b
x = spla.spsolve(A, b)

print("Solution vector x:")
print(x)
