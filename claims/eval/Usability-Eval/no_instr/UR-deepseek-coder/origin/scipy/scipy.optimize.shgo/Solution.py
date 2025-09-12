import numpy as np
from scipy.optimize import minimize

# Define the function to minimize
def objective_function(x):
    return x[0]**2 + x[1]**2

# Initial guess
initial_guess = np.array([1.0, 1.0])

# Perform SHG optimization
result = minimize(objective_function, initial_guess, method='Nelder-Mead')

# Output the result
print("Optimal solution:", result.x)
print("Minimum value:", result.fun)
