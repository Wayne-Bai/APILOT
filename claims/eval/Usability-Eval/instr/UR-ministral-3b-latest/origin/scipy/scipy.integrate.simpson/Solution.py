import numpy as np
import scipy.integrate as integrate

# User inputs
x = None
a = 0
b = 1
axis = 0

# Define the function to be integrated
def f(x):
    return np.sin(x)

# Compute the spacing of dx
if x is None:
    dx = (b - a) / 2
else:
    dx = x[1] - x[0]

# Integrate using the Composite Simpson's Rule
result, error = integrate.simps(f(a), b, dx, axis=axis)

result
