import numpy as np
from scipy.optimize import lsq_linear

# Define the linear system A * x = b
A = np.array([[1, 2], [3, 4], [5, 6]])
b = np.array([7, 8, 9])

# Set bounds for the variables (x >= 0)
bounds = (0, np.inf)

# Solve the least squares problem with bounds
result = lsq_linear(A, b, bounds=bounds)

# Display the result
print("Solution:", result.x)
print("Residuals:", result.cost)
print("Success:", result.success)
print("Message:", result.message)
