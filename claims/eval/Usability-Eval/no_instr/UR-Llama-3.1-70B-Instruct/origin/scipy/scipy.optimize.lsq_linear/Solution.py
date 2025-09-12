import scipy.optimize as optimize
import numpy as np

# Define the number of variables and the bounds
n = 4
bounds = [(0, None), (0, None), (0, None), (0, None)]

# Define the A matrix (coefficients of the linear least-squares problem)
A = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]])

# Define the b vector (right-hand side of the linear least-squares problem)
b = np.array([1, 2, 3, 4])

# Initial guess for the variables
x0 = np.array([1, 1, 1, 1])

# Solve the linear least-squares problem with bounds
res = optimize.lsq_linear(A, b, bounds=bounds, x0=x0)

# Print the result
print(res.x)
