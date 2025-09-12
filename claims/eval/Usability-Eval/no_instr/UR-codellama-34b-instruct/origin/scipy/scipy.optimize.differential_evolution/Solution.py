
import numpy as np
from scipy.optimize import minimize

def objective_function(x):
    # Replace this with your own objective function
    return x[0]**2 + x[1]**2

# Define the bounds for each variable
bounds = [(0, 1), (0, 1)]

# Define the initial guess for each variable
x0 = [0.5, 0.5]

res = minimize(objective_function, x0, method="SLSQP", bounds=bounds)

print(res.x)
