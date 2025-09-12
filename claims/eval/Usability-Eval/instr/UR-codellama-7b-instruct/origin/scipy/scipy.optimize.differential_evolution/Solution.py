from scipy.optimize import minimize
import numpy as np

# Define the multivariate function to be minimized
def f(x):
    return (x[0] - 2)**2 + (x[1] - 3)**2 + (x[2] - 4)**2

# Set the initial guess for the minimum and the bounds on each variable
x0 = np.array([1, 1, 1])
bounds = [(0, 1), (0, 1), (0, 1)]

# Use the minimize function from SciPy to find the global minimum
res = minimize(f, x0, bounds=bounds)

# Print the result
print(res.x)
