
import numpy as np
from scipy.optimize import minimize

def objective_function(x, a, b):
    # Define the function to be fitted to the data
    return a * np.sin(b * x)

def residuals(params, x, y):
    # Calculate the residual between the model and the data
    return (y - objective_function(x, params[0], params[1])) ** 2

def least_squares(x, y, a0, b0):
    # Initialize the initial guesses for the parameters
    params = np.array([a0, b0])
    
    # Use the scipy minimize function to find the best fit parameters
    result = minimize(residuals, params, args=(x, y))
    
    return (result.fun, result.x)
