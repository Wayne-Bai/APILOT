import numpy as np
from scipy.optimize import minimize

# Define the function for which we want to find the global minimum
def objective_function(x):
    return x**2 + 10 * np.sin(x)

# Set the initial guess
initial_guess = 0.0

# Use the minimize function with a method suitable for global optimization
result = minimize(objective_function, initial_guess, method='BFGS')

# Print the result
print("Global minimum found at:", result.x)
print("Objective function value at minimum:", result.fun)
