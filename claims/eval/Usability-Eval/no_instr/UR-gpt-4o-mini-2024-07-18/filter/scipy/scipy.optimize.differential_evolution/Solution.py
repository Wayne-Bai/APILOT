import numpy as np
from scipy.optimize import minimize

# Define the multivariate function
def objective_function(x):
    # Example: a simple quadratic function
    return np.sum(x**2)

# Set the initial guess
initial_guess = np.array([1.0, 1.0])

# Use 'L-BFGS-B' method for minimization
result = minimize(objective_function, initial_guess, method='L-BFGS-B')

# Print the results
print("Global minimum found at:", result.x)
print("Objective function value at minimum:", result.fun)
