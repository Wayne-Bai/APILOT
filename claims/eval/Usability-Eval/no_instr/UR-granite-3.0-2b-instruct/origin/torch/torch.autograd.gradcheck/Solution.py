import torch

# Create a tensor with requires_grad=True
x = torch.tensor(1.0, requires_grad=True)

# Compute gradients using finite differences
h = 1e-5
x_plus = x + h
x_minus = x - h
grad_numerical = (x_plus.grad - x_minus.grad) / (2 * h)

# Compute analytical gradients
x.grad = torch.ones_like(x)
grad_analytical = x.grad

# Print gradients
print("Numerical gradient:", grad_numerical)
print("Analytical gradient:", grad_analytical)
