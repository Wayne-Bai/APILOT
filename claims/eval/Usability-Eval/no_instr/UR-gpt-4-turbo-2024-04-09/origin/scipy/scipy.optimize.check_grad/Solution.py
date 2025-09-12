import numpy as np
from scipy.optimize import check_grad

def func(x):
    """ Define the function for which you want to check the gradient. """
    return x[0]**2 + x[1]**2

def grad(x):
    """ Provide the analytical gradient of the function. """
    return np.array([2*x[0], 2*x[1]])

def forward_finite_diff(func, x, h=1e-8):
    """ Finite difference approximation of the gradient. """
    n = len(x)
    grad_approx = np.zeros(n)
    fx = func(x)
    for i in range(n):
        x1 = np.array(x, copy=True)
        x1[i] += h
        fxi = func(x1)
        grad_approx[i] = (fxi - fx) / h
    return grad_approx

# Example usage:
x = np.array([1.0, 2.0])
error = check_grad(func, grad, x, epsilon=1e-8)
print(f"Gradient check error: {error}")
