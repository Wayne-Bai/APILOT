
import numpy as np
from scipy.sparse import spdiags
from scipy.sparse.linalg import spsolve

# Define the sparse matrix A
# Example: Creating a tridiagonal matrix as an example
n = 5
diagonals = [[-1, 2, -1], [-1, 2, -1], [-1, 2, -1]]
offsets = [-1, 0, 1]
A = spdiags(diagonals, offsets, n, n).toarray()

# Define the right-hand side vector b (can be a vector or a matrix)
b = np.array([1, 2, 3, 4, 5])

# Solve the sparse linear system Ax=b
x = spsolve(A, b)

print("Solution x:")
print(x)
