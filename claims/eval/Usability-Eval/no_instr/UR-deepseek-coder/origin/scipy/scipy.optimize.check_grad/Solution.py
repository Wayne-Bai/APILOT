import numpy as np
from scipy.optimize import approx_fprime

def gradient_function(x):
    # Example gradient function, replace with your actual gradient function
    return 2 * x

def function_to_differentiate(x):
    # Example function, replace with your actual function
    return x**2

def check_gradient(func, grad_func, x0, epsilon=1e-8):
    # Compute the finite-difference approximation of the gradient
    fd_gradient = approx_fprime(x0, func, epsilon)
    
    # Compute the analytical gradient
    analytical_gradient = grad_func(x0)
    
    # Compare the two gradients
    print("Finite-difference gradient:", fd_gradient)
    print("Analytical gradient:", analytical_gradient)
    
    # Compute the relative error
    relative_error = np.linalg.norm(fd_gradient - analytical_gradient) / np.linalg.norm(analytical_gradient)
    print("Relative error:", relative_error)
    
    return relative_error

# Example usage
x0 = np.array([1.0])  # Initial point
check_gradient(function_to_differentiate, gradient_function, x0)
