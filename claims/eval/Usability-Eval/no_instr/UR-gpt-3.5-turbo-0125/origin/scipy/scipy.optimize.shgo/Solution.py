
import numpy as np
from scipy.optimize import shgo

# Define the objective function to be minimized
def objective(x):
    return x[0]**2 + x[1]**2

# Define the bounds for each variable
bounds = [(-1.0, 1.0), (-1.0, 1.0)]

# Use SHG optimization to find the global minimum
result = shgo(objective, bounds)

# Print the global minimum found
print("Global minimum: ", result.fun)
print("Optimal point: ", result.x)
