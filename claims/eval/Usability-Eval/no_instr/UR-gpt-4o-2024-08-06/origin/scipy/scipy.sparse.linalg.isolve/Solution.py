import numpy as np
from scipy.sparse import csc_matrix
from scipy.sparse.linalg import splu

# Example sparse matrix A
A = csc_matrix([
    [3, 1, 0],
    [1, 2, 0],
    [0, 0, 1]
])

# Vector b
b = np.array([5, 5, 3])

# Solve Ax = b
lu = splu(A)
x = lu.solve(b)

print("Solution x:", x)
