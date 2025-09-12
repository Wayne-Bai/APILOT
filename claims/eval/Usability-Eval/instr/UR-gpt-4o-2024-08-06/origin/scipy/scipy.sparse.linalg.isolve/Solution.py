import numpy as np
from scipy.sparse import csc_matrix
from scipy.sparse.linalg import spsolve

# Example sparse matrix A
data = np.array([1, 2, 3, 4, 5])
i = np.array([0, 1, 2, 0, 1])
j = np.array([0, 1, 2, 1, 2])
A = csc_matrix((data, (i, j)), shape=(3, 3))

# Example vector b
b = np.array([1, 2, 3])

# Solve the system Ax = b
x = spsolve(A, b)

print("Solution vector x:", x)
