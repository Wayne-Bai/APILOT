import numpy as np
from scipy.optimize import minimize

# Define the multivariate function
def func(x):
    # Example function: This is the Rosenbrock function
    # which is a common test problem for optimization algorithms.
    return sum(100.0 * (x[1:] - x[:-1]**2.0)**2.0 + (1 - x[:-1])**2.0)

# Set initial guess for the variables
initial_guess = np.array([0.0, 0.0])

# Use the 'minimize' function from scipy.optimize
result = minimize(func, initial_guess, method='BFGS')

# Print the result
if result.success:
    print('Optimization succeeded.')
    print('Global minimum found at:', result.x)
    print('Function value at minimum:', result.fun)
else:
    print('Optimization failed.')
