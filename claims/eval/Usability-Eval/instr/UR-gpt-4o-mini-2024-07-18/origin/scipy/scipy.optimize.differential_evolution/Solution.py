import numpy as np
from scipy.optimize import minimize

# Define the multivariate function to minimize
def objective_function(x):
    return np.sum(x**2)  # Example: simple quadratic function

# Initial guess
initial_guess = np.array([1.0, 1.0])

# Find the global minimum
result = minimize(objective_function, initial_guess, method='BFGS')

# Output the result
print("Global minimum found at:", result.x)
print("Minimum value:", result.fun)
