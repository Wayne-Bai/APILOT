import numpy as np
from scipy.optimize import dual_annealing

# Example function: Let's use a simple multi-modal function
def objective_function(x):
    return np.sin(3 * x) + x**2 - 0.7*x

# Define the bounds for the variable
bounds = [(-2, 2)]  # x is between -2 and 2

# Perform the global optimization using Simulated Annealing
result = dual_annealing(objective_function, bounds)

print("Global minimum value:", result.fun)
print("At x:", result.x)
