
import numpy as np
from scipy.optimize import minimize

# Define the multivariate function
def multivariate_function(x):
    return x[0]**2 + x[1]**2 + x[0]*x[1] + np.sin(x[0])

# Find the global minimum
initial_guess = [0, 0]
result = minimize(multivariate_function, initial_guess, method='Nelder-Mead')

print("Global minimum found at:", result.x)
