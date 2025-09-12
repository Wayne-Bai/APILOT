import numpy as np
from scipy.optimize import differential_evolution

# Define the objective function to minimize
def objective_function(x):
    return x[0]**2 + x[1]**2 + x[0]*x[1] - 10

# Define the bounds for each variable in the function
bounds = [(-10, 10), (-10, 10)]

# Find the global minimum using Differential Evolution
result = differential_evolution(objective_function, bounds)

# Print the results
print('Global minimum:', result.x)
print('Function value at global minimum:', result.fun)
