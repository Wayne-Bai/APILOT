import scipy.optimize as opt
import numpy as np

# Define the matrix A and vector b for the linear system Ax = b
A = np.array([[1, 2], [3, 4]])
b = np.array([1, 4])

# Define lower and upper bounds for the variables
lower_bounds = [0, 0]  # x >= 0
upper_bounds = [np.inf, np.inf]  # no upper bound

# Solve the bounded linear least-squares problem
result = opt.lsq_linear(A, b, bounds=(lower_bounds, upper_bounds))

# Print results
print("Optimal solution:", result.x)
print("Status message:", result.message)
