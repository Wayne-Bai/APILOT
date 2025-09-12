import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import spsolve

# Define A and b
A = np.array([[3, 2], [1, 1]])  # This should be your sparse matrix
b = np.array([9, 4])  # This could be a vector or a matrix

# Convert A to a Compressed Sparse Row (CSR) matrix
A = csr_matrix(A)

# Solve for x
x = spsolve(A, b)

print(x)
