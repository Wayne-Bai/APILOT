import numpy as np
from scipy.optimize import shgo

# Define the function we want to find minimum for. For example: f(x) = x^2
def func(x):
    return x[0]**2

# Define the boundaries within which we want to find the minimum.
# Here, we take x to be in the range [-100, 100].
ranges = [(-100, 100)]

# Use SHG optimization to find the global minimum.
res = shgo(func, ranges)

# res.x contains the solution.
minimum_solution = res.x
print(f'The global minimum of function f(x) = x^2 is at x = {minimum_solution}')
