import numpy as np
from scipy.optimize import check_grad

def gradient_function(x):
    # Implement your gradient function here
    # For example, let's consider a simple function f(x) = x^2
    return 2 * x

def finite_difference_gradient(x, h=1e-7):
    # Compute the gradient using finite difference approximation
    grad = np.zeros_like(x)
    for i in range(len(x)):
        x_plus_h = x.copy()
        x_plus_h[i] += h
        grad[i] = (gradient_function(x_plus_h) - gradient_function(x)) / h
    return grad

# Generate random input
x = np.random.rand(10)

# Check the correctness of the gradient function
max_abs_diff = check_grad(gradient_function, finite_difference_gradient, x)
print(f"Maximum absolute difference: {max_abs_diff}")
