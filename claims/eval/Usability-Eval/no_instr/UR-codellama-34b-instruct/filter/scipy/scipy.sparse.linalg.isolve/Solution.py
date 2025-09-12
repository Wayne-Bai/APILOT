
import numpy as np
from scipy.sparse import linalg as sla

# Define the matrix A and vector b
A = np.array([[1, 2], [3, 4]])
b = np.array([5, 6])

# Convert A and b to sparse matrices
A_sp = sla.csr_matrix(A)
b_sp = sla.csr_vector(b)

# Solve the linear system using the sparse solver
x = sla.spsolve(A_sp, b_sp)

# Convert x to a dense vector
x_dense = np.array(x)

print("Solution:", x_dense)
