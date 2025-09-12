# Import necessary libraries
import numpy as np
from scipy.optimize import least_squares

# Define the function to minimize
def residual(params, x, y):
    """
    The residual function to minimize.
    
    Parameters
    ----------
    params : array_like
        The model parameters.
    x : array_like
        The independent variable.
    y : array_like
        The dependent variable.
    
    Returns
    -------
    array_like
        The residual between the model and the data.
    """
    return params[0] * x + params[1] - y

# Generate some sample data
np.random.seed(0)
x = np.linspace(0, 10, 100)
y = 2.5 * x + 1.5 + np.random.normal(0, 2, 100)

# Initial guess for the parameters
params_guess = [1.0, 0.0]

# Lower and upper bounds for the parameters
bounds = ([0.0, -10.0], [10.0, 10.0])

# Solve the least-squares problem
result = least_squares(residual, params_guess, args=(x, y), bounds=bounds)

# Print the results
print(f"Parameters: {result.x}")
print(f"Success: {result.success}")
print(f"Covariance: {result.jac}")
print(f"Residuals: {result.fun}")
