import numpy as np
from scipy.misc import derivative
import math

# Define the function and its gradient
def f(x):
    return np.sum(x**2)

def gradient_f(x, h=1e-7):
    grad = np.zeros(len(x))
    for i in range(len(x)):
        x_plus_h = np.copy(x)
        x_plus_h[i] += h
        x_minus_h = np.copy(x)
        x_minus_h[i] -= h
        grad[i] = (f(x_plus_h) - f(x_minus_h)) / (2.0 * h)
    return grad

# Define the analytical gradient function
def analytical_gradient_f(x):
    return 2 * x

# Test the gradient function
x = np.array([1.0, 2.0, 3.0, 4.0, 5.0])

# Compute the gradient using the gradient function
grad_f = analytical_gradient_f(x)

# Compute the gradient using finite differences
grad_fd = gradient_f(x)

# Print the results
print("Analytical Gradient: ", grad_f)
print("Finite Difference Gradient: ", grad_fd)

# Check the correctness of the gradient function
print("Difference between gradients: ", np.linalg.norm(grad_f - grad_fd))
print("Relative difference between gradients: ", np.linalg.norm(grad_f - grad_fd) / np.linalg.norm(grad_f))
