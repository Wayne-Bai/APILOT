import numpy as np
from scipy.optimize import minimize

# Define your multivariate function here
def multivariate_func(x):
    return (x[0] - 1)**2 + (x[1] - 2.5)**2

# Initial guess for the variables
initial_guess = [2, 0]

# Use minimize function to find the global minimum
result = minimize(multivariate_func, initial_guess)

print('The global minimum occurs at: ', result.x)
