
import numpy as np
from scipy.optimize import minimize

# Define the multivariate function
def multivariate_function(x):
    return x[0]**2 + x[1]**2 + x[2]**2

# Initial guess
initial_guess = [1, 1, 1]

# Find the global minimum
result = minimize(multivariate_function, initial_guess, method='Nelder-Mead')

# Print the result
print('Global minimum found at:', result.x)
