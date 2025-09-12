# Importing necessary libraries
import torch
import torch.autograd as autograd
import numpy as np

# Set the seed for reproducibility
torch.manual_seed(42)
np.random.seed(42)

# Define a function to compute analytical gradient
def analytical_gradient(x, classification=True):
    """
    Compute the analytical gradient of a function.
    If classification, the function returns a vector.
    Otherwise, the function returns a scalar.
    """
    if classification:
        # For binary classification, the function is f(x) = -x^2
        # and its analytical gradient is df/dx = -2x
        return -2*x
    else:
        # For regression, the function is f(x) = x^2
        # and its analytical gradient is df/dx = 2x
        return 2*x

# Define a function to check gradients via small finite differences
def check_gradients_finite_diff(x, classification=True):
    """
    Check gradients computed via small finite differences against analytical gradients.
    """
    # Create a small perturbation
    delta = torch.zeros_like(x) + torch.tensor(1e-6)
    # Compute forward pass for perturbed x
    f_delta = analytical_gradient(x + delta, classification)
    # Compute forward pass for unperturbed x
    f = analytical_gradient(x, classification)
    # Compute gradient via small finite differences
    grad_finite_diff = (f_delta - f) / delta
    # Compute analytical gradient
    grad_analytical = analytical_gradient(x, classification)
    # Check if the two gradients are equal
    assert torch.allclose(grad_finite_diff, grad_analytical), "Gradient mismatch"

# Generate random inputs with requires_grad=True
x = autograd.Variable(torch.randn(1) + 1j*torch.randn(1), requires_grad=True)
x_float = autograd.Variable(torch.randn(1).float(), requires_grad=True)

# Check gradients for floating point inputs
check_gradients_finite_diff(x_float.float(), classification=False)
check_gradients_finite_diff(x_float, classification=True)

# Check gradients for complex inputs
check_gradients_finite_diff(x, classification=False)
check_gradients_finite_diff(x, classification=True)
