from scipy import sparse, linalg

# Create a sparse matrix A and a vector b
# For example, let A be a sparse matrix with 10 rows and 10 columns, and b be a vector with 10 elements
# You can use scipy.sparse.random to generate a random sparse matrix

# Generate a random sparse matrix A and a vector b
import scipy.sparse as sp
import numpy as np

# Create a random sparse matrix A with 10 rows and 10 columns
A = sp.random(10, 10, density=0.1, format='csr')

# Create a vector b with 10 elements
b = np.random.rand(10)

# Solve the sparse linear system Ax=b
x = linalg.sparse.spsolve(A, b)

# Print the solution x
print(x)
