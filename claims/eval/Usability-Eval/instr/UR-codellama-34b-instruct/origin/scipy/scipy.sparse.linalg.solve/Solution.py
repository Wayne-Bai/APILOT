import numpy as np
from scipy.sparse import linalg

# Define the sparse matrix A and the right-hand side b
A = np.array([[1, 0, 2], [3, 4, 5]])
b = np.array([6, 7])

# Solve the system using LU decomposition
lu, piv = linalg.lu(A)
x = linalg.solve_triangular(lu, b, lower=True)

# Print the solution
print(x)
