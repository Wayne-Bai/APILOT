import numpy as np
from scipy.optimize import shgo

# Define the function to minimize
def objective_function(x):
    return (x[0] - 1)**2 + (x[1] - 2.5)**2

# Define the bounds for the variables
bounds = [(0, 5), (0, 5)]

# Perform the SHGO optimization
result = shgo(objective_function, bounds)

# Print the results
print("Global minimum found at:")
print("x =", result.x)
print("f(x) =", result.fun)
