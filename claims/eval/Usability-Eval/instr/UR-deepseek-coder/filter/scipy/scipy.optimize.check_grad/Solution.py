import numpy as np
from scipy.optimize import approx_fprime

def check_gradient(func, grad_func, x0, epsilon=1e-8):
    """
    Check the correctness of a gradient function by comparing it against a 
    (forward) finite-difference approximation of the gradient.

    Parameters:
    func : callable
        The function to compute the gradient of.
    grad_func : callable
        The gradient function to be checked.
    x0 : array_like
        The point at which to check the gradient.
    epsilon : float, optional
        The step size for the finite difference approximation.

    Returns:
    diff : float
        The maximum absolute difference between the analytical gradient and the finite difference approximation.
    """
    # Compute the analytical gradient
    analytical_grad = grad_func(x0)
    
    # Compute the finite difference approximation
    finite_diff_grad = approx_fprime(x0, func, epsilon)
    
    # Compute the maximum absolute difference
    diff = np.max(np.abs(analytical_grad - finite_diff_grad))
    
    return diff

# Example usage:
def example_func(x):
    return x[0]**2 + x[1]**3

def example_grad(x):
    return np.array([2*x[0], 3*x[1]**2])

x0 = np.array([1.0, 2.0])
diff = check_gradient(example_func, example_grad, x0)
print(f"Maximum absolute difference: {diff}")
