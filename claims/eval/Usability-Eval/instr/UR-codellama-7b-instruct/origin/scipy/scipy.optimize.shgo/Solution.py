
import numpy as np
from scipy.optimize import minimize

def f(x):
    return x**2 + 1

# Define the bounds for the optimization
bounds = [(0, None), (None, None)]

# Initialize the SHG optimizer
shg = SHGO(f, bounds)

# Find the global minimum of the function using SHG optimization
min_x = shg.optimize()
