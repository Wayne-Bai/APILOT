import numpy as np
from scipy.misc import derivative

# Define a function for which we want to check the gradient
def f(x):
    return x**2

# Define a grid for x values
x = np.linspace(-10, 10, 1000)

# Calculate the true gradient of the function
df_dx = 2 * x

# Calculate the finite-difference approximation of the gradient
df_dx_fd = (f(x + 1e-5) - f(x - 1e-5)) / (2 * 1e-5)

# Check the correctness of the gradient function
assert np.allclose(df_dx, df_dx_fd), "The gradient function is not correct"
