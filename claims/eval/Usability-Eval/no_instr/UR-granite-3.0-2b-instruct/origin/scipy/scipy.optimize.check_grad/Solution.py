import numpy as np
from scipy.optimize import minimize

# Define the function for which we want to check the gradient
def f(x):
    return np.sum(x**2)

# Define the gradient function
def grad_f(x):
    return 2 * x

# Define the function to calculate the finite-difference approximation of the gradient
def fin_diff_grad(x, h=1e-5):
    grad_approx = (f(x + h) - f(x - h)) / (2 * h)
    return grad_approx

# Define the function to check the correctness of the gradient function
def check_gradient(f, grad_f, x, tol=1e-5):
    grad_approx = fin_diff_grad(x)
    grad_diff = np.abs(grad_f(x) - grad_approx)
    return grad_diff

# Define the initial point
x0 = np.array([1.0, 1.0])

# Define the tolerance
tol = 1e-5

# Check the correctness of the gradient function
grad_diff = check_gradient(f, grad_f, x0)
print(f"The difference between the analytical and finite-difference approximations of the gradient is {grad_diff:.2e}")
