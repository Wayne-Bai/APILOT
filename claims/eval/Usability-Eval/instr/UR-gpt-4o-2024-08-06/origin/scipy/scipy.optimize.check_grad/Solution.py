import numpy as np
from scipy.optimize import approx_fprime

def finite_difference_grad_check(func, x0, grad_func, epsilon=1e-8):
    """
    Check the correctness of a gradient function by comparing it against a 
    finite-difference approximation of the gradient.

    Parameters:
    func : callable
        The function for which the gradient is computed.
    x0 : array_like
        The point at which the gradient is checked.
    grad_func : callable
        The gradient function to be checked.
    epsilon : float, optional
        The step size for finite difference.

    Returns:
    bool
        True if the computed gradient is close to the numerical gradient, False otherwise.
    """
    # Compute the analytic gradient at x0
    analytic_grad = grad_func(x0)
    
    # Compute the numerical gradient using forward finite-difference approximation
    num_grad = approx_fprime(x0, func, epsilon)
    
    # Calculate the relative error
    rel_error = np.linalg.norm(analytic_grad - num_grad) / max(np.linalg.norm(analytic_grad), np.linalg.norm(num_grad), 1e-8)

    print(f"Analytic Gradient: {analytic_grad}")
    print(f"Numerical Gradient: {num_grad}")
    print(f"Relative Error: {rel_error}")

    # Check if the gradients are similar
    return rel_error < 1e-5

# Example usage
def example_func(x):
    return np.dot(x, x)

def example_grad(x):
    return 2 * x

x0 = np.array([1.0, 2.0, 3.0])

# Check the gradient
is_correct = finite_difference_grad_check(example_func, x0, example_grad)
print(f"Gradient correct: {is_correct}")
