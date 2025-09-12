import numpy as np
from scipy.optimize import check_grad

def forward_gradient(func, x, eps=1e-8):
    grad = np.zeros_like(x)
    for i in range(x.size):
        e = np.zeros_like(x)
        e[i] = eps
        grad[i] = (func(x + eps*e) - func(x)) / eps
    return grad

def check_gradient(func, grad_func, x):
    return check_grad(func, grad_func, x)

# Example usage:
def example_func(x):
    return np.sum(x**2)

def example_grad(x):
    return 2*x

x = np.array([1.0, 2.0, 3.0])

print(check_gradient(example_func, example_grad, x))
