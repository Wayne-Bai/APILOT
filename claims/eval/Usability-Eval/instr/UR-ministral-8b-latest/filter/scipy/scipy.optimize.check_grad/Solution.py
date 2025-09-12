import numpy as np
from scipy.optimize import approx_fprime

# Example gradient function
def gradient_function(x):
    return np.array([x[0]**2 + x[1], -x[0] + x[1]**2])

# Coordinate (x, y) at which to evaluate the gradient
x_coords = np.array([1.0, 2.0])

# Compute analytical gradient
analytical_gradient = gradient_function(x_coords)

# Compute the finite difference approximation
finite_diff_gradient = approx_fprime(x_coords, gradient_function, dx=1e-5)

# Compare the two gradients
relative_error = np.abs(analytical_gradient - finite_diff_gradient) / np.abs(analytical_gradient)

# Display the results
print("Analytical Gradient:", analytical_gradient)
print("Finite Difference Gradient:", finite_diff_gradient)
print("Relative Error:", relative_error)
