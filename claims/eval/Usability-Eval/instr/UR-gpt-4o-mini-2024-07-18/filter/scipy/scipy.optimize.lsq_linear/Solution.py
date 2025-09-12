import numpy as np
from scipy.optimize import lsq_linear

# Example data for demonstration
A = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])
b = np.array([1, 2, 2, 3])

# Define bounds on the variables, for example, x0 >= 0 and x1 >= 0
bounds = (0, np.inf)  # lower bound is 0, upper bound is infinity

# Solve the linear least-squares problem with bounds
result = lsq_linear(A, b, bounds=bounds)

# Output the result
print("Optimal solution:", result.x)
print("Cost:", result.cost)
