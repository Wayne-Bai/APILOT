import scipy.sparse as sp
import scipy.sparse.linalg as spla
import numpy as np

# Define A and b
A = sp.csc_matrix([[3, 2, 0], [1, -1, 0], [0, 5, 1]])
b = np.array([2, 4, -1])

# Solve the sparse linear system
x = spla.spsolve(A, b)
print("Solution:\n", x)
