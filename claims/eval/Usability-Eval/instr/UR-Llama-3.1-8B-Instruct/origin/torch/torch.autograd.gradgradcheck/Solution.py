import torch
import torch.autograd
import torch.autograd.functional
import numpy as np

# Create some inputs and grad_outputs
x = torch.randn(2, dtype=torch.float64, requires_grad=True)
y = torch.randn(2, dtype=torch.complex128, requires_grad=True)
grad_output = torch.randn(2, dtype=torch.float64)

# Compute the gradients of the gradient wrt the inputs
x_grad = torch.autograd.grad(grad_output.sum(), x, create_graph=True)[0]
y_grad = torch.autograd.grad(grad_output.sum(), y, create_graph=True)[0]

# Compute the analytical gradients
def foo(x, y):
    return (x**2 + y**2).sum()

x_grad_analytic = torch.autograd.grad(foo(x, y), x, grad_outputs=torch.ones(2), retain_graph=True)[0]
y_grad_analytic = torch.autograd.grad(foo(x, y), y, grad_outputs=torch.ones(2), retain_graph=True)[0]

# Compute the small finite differences to estimate the gradients
epsilon = 1e-6
x_grad_finite_diff = (foo(x + epsilon*torch.ones(2), y) - foo(x - epsilon*torch.ones(2), y)) / (2 * epsilon)
y_grad_finite_diff = (foo(x, y + epsilon*torch.ones(2)) - foo(x, y - epsilon*torch.ones(2))) / (2 * epsilon)

# Check if the gradients computed via small finite differences are close to the analytical gradients
torch.autograd.grad_check(x_grad_finite_diff, x_grad_analytic)
torch.autograd.grad_check(y_grad_finite_diff, y_grad_analytic)
