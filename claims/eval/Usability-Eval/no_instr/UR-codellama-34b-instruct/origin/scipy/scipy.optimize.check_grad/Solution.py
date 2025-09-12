import numpy as np
from scipy.misc import derivative

def gradient_function(x):
    # Your gradient function implementation here
    return None

# Define a test point and step size for finite difference approximation
x = np.array([1, 2, 3])
h = 0.01

# Compute forward finite difference approximation of gradient
f_fd = derivative(lambda x: f(x), x, h)

# Compare with output of your gradient function
g_analytical = gradient_function(x)
print("Analytical gradient:", g_analytical)
print("Finite difference approximation:", f_fd)
