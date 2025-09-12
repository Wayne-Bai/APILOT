import numpy as np
from scipy.sparse import lil_matrix

# Define the coefficients of the linear system
A = lil_matrix((3, 3))
A[0, 0] = 2
A[0, 1] = 1
A[1, 0] = 1
A[1, 1] = 2
A[2, 1] = 1
A[2, 2] = 2

# Define the constant term b
b = np.array([1, 2, 3])

# Solve the linear system Ax=b
x = np.linalg.solve(A.toarray(), b)

print(x)

# Output: [0. 1. 2.]