import numpy as np
from scipy.optimize import least_squares

# Define the function we want to fit
def f(x, a, b):
    return a * np.sin(b * x)

# Generate some random data
np.random.seed(0)
x = np.sort(10 * np.random.rand(20))
y = f(x, 2.5, 1.3) + np.random.randn(len(x))

# Define the residuals function
def residuals(p, x, y):
    a, b = p
    return f(x, a, b) - y

# Initial guess for the parameters
p0 = [1, 1]

# Perform the non-linear least squares fit
res = least_squares(residuals, p0, args=(x, y))

# Get the optimal parameters
a_fit, b_fit = res.x

print(f"Fit results: a = {a_fit}, b = {b_fit}")
