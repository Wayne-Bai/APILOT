import numpy as np
from scipy.optimize import minimize

# Define the problem
A = np.array([[1, 2], [3, 4]])
b = np.array([5, 6])
x_bounds = (0, 1)

# Define the objective function and constraints
def obj(x):
    return (A @ x - b) ** 2

def bounds(x):
    return x_bounds[0] <= x <= x_bounds[1]

# Solve the problem
res = minimize(obj, x_bounds, method="SLSQP", constraints=bounds)

# Print the solution
print("Solution:")
print(res.x)
