from scipy.optimize import least_squares
import numpy as np

# Define the residual function
def residual_function(x):
    # Replace this with your own residual function
    return np.array([x[0]**2 + x[1]**2 - 1])

# Define the bounds for the variables
bounds = [(None, None), (None, None)]  # Replace with your own bounds

# Define the initial guess for the variables
x0 = np.array([1.0, 1.0])

# Solve the linear least-squares problem with bounds
result = least_squares(residual_function, x0, bounds=bounds)

# Print the solution
print("Solution: ", result.x)
