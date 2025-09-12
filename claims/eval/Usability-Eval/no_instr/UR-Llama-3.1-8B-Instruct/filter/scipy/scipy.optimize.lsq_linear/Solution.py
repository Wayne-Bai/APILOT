from scipy.optimize import least_squares
import numpy as np

# Coefficients for the linear equation
A = np.array([[3, 1], [1, 2], [2, 1]])

# Inhomogeneities of the linear equation
b = np.array([6, 5, 8])

# Initial guess
x0 = np.array([0, 0])

# Bounds for the variables
bounds = [(0, None), (0, None)]

# Solve the linear least-squares problem with bounds
result = least_squares(lambda x: A @ x - b, x0, bounds=bounds)

# Print the solution
print("Solution: ", result.x)
