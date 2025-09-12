import numpy as np
from scipy.sparse import csr_matrix, linalg

# Define the sparse matrix A
A = csr_matrix(([1, 2, 3], ([0, 0, 1], [0, 1, 2])), shape=(3, 3))

# Define the right-hand side vector b
b = np.array([1, 2, 3])

# Solve the system Ax=b using spsolve
x = linalg.spsolve(A, b)

# Print the solution
print(x)
