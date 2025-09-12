import numpy as np
from scipy.optimize import lsq_linear

# Example data
A = np.array([[1, 2], [3, 4], [5, 6]])
b = np.array([7, 8, 9])

# Bounds for the variables
lb = np.array([0, 0])  # Lower bound
ub = np.array([5, 5])  # Upper bound

# Solve the least squares problem with bounds
result = lsq_linear(A, b, bounds=(lb, ub))

# Output the result
print("Optimal solution:", result.x)
print("Cost function value:", result.cost)
print("Success:", result.success)
print("Message:", result.message)
