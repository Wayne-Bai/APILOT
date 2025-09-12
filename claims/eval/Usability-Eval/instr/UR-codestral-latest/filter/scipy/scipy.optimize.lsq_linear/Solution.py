import numpy as np
from scipy.optimize import lsq_linear, Bounds, minimize

# Let's assume for example purposes:
A = np.array([[1, 2], [3, 4]])
b = np.array([5, 6])

# Variables' bounds
bounds = Bounds(0, np.inf)  # replace with actual bounds

# Solving the least-squares problem
res = lsq_linear(A, b, bounds=bounds)

# apply_bounds function to apply the bounds
def apply_bounds(x, bounds):
    return np.maximum(bounds.lb, np.minimum(bounds.ub, x))

# This will apply the bounds
x = apply_bounds(res.x, bounds)
