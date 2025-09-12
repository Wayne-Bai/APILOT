import numpy as np
from scipy.optimize import lsq_linear

# Example: Ax = b
A = np.array([[1, 1], [1, 1], [2, 2]])
b = np.array([1, 1, 1])

# Define bounds for each variable
lower_bounds = [0, 0]  # Lower bounds for x1 and x2
upper_bounds = [1, 2]  # Upper bounds for x1 and x2

# Solve the bounded linear least-squares problem
res = lsq_linear(A, b, bounds=(lower_bounds, upper_bounds))

print("Solution to the linear least squares problem with bounds:", res.x)
print("Optimal cost:", res.cost)
