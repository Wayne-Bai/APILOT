import numpy as np
from scipy.optimize import approx_fprime

def gradient_check(func, x, epsilon=1e-8):
    """
    Check the correctness of a gradient function by comparing it 
    against a finite-difference approximation of the gradient.

    Parameters:
    func : callable
        The function for which the gradient is being checked. 
        Should take a single argument (numpy array).
    x : numpy array
        The point at which to check the gradient.
    epsilon : float
        The small perturbation value for finite difference approximation.

    Returns:
    bool
        True if the analytical gradient matches the finite difference approximation, False otherwise.
    """
    # Analytical gradient (should be provided by user)
    analytical_grad = compute_gradient(func, x)

    # Finite difference approximation of the gradient
    finite_diff_grad = approx_fprime(x, func, epsilon)

    # Compare the two gradients
    return np.allclose(analytical_grad, finite_diff_grad, atol=epsilon)

def compute_gradient(func, x):
    # Example of how to compute the analytical gradient (user-defined)
    # Replace this with an actual implementation based on your function
    gradient = np.zeros_like(x)
    # Compute gradient (placeholder code, should be replaced)
    gradient[0] = 2 * x[0]  # Example: derivative of x^2 wrt x
    return gradient
