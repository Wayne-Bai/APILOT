from scipy.sparse import csr_matrix
from scipy.sparse.linalg import spsolve
import numpy as np

# Define the sparse matrix A and vector/matrix b
# Example:
# A = csr_matrix([[3, 0, 0], [0, 2, 0], [0, 0, 1]])
# b = np.array([[1], [2], [3]]) or np.array([[1, 2], [3, 4], [5, 6]])

# Solve the sparse linear system
x = spsolve(A, b)

# Print the solution
print("The solution x is:", x)
