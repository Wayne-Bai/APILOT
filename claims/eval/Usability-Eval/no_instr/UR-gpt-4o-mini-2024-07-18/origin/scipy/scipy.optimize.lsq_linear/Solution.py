import numpy as np
from scipy.optimize import lsq_linear

# Example data for the linear least-squares problem
# Design matrix
A = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
# Observations
b = np.array([1, 2, 2, 3])
# Bounds on the variables
lb = np.array([0, 0])  # Lower bounds
ub = np.array([3, 3])  # Upper bounds

# Solve the linear least-squares problem with bounds
result = lsq_linear(A, b, bounds=(lb, ub))

# Output the result
print("Optimal Solution:", result.x)
print("Cost:", result.cost)
