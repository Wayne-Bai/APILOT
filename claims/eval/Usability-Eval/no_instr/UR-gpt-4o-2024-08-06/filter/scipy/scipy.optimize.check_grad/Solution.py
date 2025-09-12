import numpy as np
from scipy.optimize import approx_fprime

def compute_gradient(f, x, epsilon=1e-8):
    """
    Computes the finite-difference approximation of the gradient of a scalar field function
    using forward difference method.
    
    Parameters:
        f (callable): The scalar field function.
        x (np.array): The point at which the gradient is evaluated.
        epsilon (float): The step size used to approximate the gradient.
        
    Returns:
        gradient (np.array): The approximated gradient.
    """
    gradient = approx_fprime(x, f, epsilon)
    return gradient

def example_function(x):
    # Example function, such as f(x) = x1^2 + x2^2 + x3^2
    return np.sum(x**2)

def analytic_gradient(x):
    # The analytical gradient of the example function: grad(x) = [2*x1, 2*x2, 2*x3]
    return 2 * x

# Test the gradient calculation:
x0 = np.array([1.0, 2.0, 3.0])  # Initial point

numerical_grad = compute_gradient(example_function, x0)
analytical_grad = analytic_gradient(x0)

print("Numerical Gradient:", numerical_grad)
print("Analytical Gradient:", analytical_grad)
print("Difference:", np.linalg.norm(numerical_grad - analytical_grad))
