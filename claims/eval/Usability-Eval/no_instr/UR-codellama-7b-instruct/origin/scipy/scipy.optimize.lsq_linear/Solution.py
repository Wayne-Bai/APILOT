import numpy as np
from scipy.optimize import minimize

# Define the objective function to be minimized
def obj_func(x):
    return (x[0] - 2)**2 + (x[1] - 3)**2

# Define the bounds for each variable
bounds = [(0, 5), (0, 10)]

# Minimize the objective function with bounds
res = minimize(obj_func, x0=[1, 2], method='SLSQP', bounds=bounds)

print(res.x)
