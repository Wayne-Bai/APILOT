import torch

# Set up parameters
input_tensor = torch.randn(2, requires_grad=True)
grad_output = torch.randn(2, requires_grad=True)
epsilon = 1e-7

# Compute numerical gradient using finite differences
alpha = torch.randn_like(input_tensor) + epsilon
alpha.requires_grad = False

input_tensor.grad = grad_output + torch.autograd.grad(alpha + input_tensor * gradient_output, input_tensor)[0]

# Analytical gradient
analytical_gradient = torch.autograd.grad(input_tensor, grad_output)[0]

# Compute gradients of gradients
grad_of_grad_numerical = torch.autograd.grad(input_tensor, input_tensor)[0]
grad_of_grad_analytical = torch.autograd.grad(grad_output, grad_output)[0]

# Compare numerical and analytical gradients
print("Numerical gradient: ", grad_of_grad_numerical)
print("Analytical gradient: ", grad_of_grad_analytical)
print("Difference: ", torch.abs(grad_of_grad_numerical - grad_of_grad_analytical))
