import numpy as np
from scipy.optimize import lsq_linear

# Define the matrix A and vector b for the linear system Ax = b
A = np.array([[1, 2], [3, 4], [5, 6]])
b = np.array([1, 2, 3])

# Define the bounds for the variables
# (lower bound, upper bound) for each variable
bounds = ([-1, -1], [1, 1])

# Solve the linear least-squares problem with bounds on the variables
result = lsq_linear(A, b, bounds=bounds)

# Print the solution
print("Solution:", result.x)
print("Residual norm:", result.cost)
