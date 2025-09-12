import torch
import torch.nn as nn

# Define a model with parameters that require gradients
model = nn.Sequential(
    nn.Linear(5, 10),
    nn.ReLU(),
    nn.Linear(10, 20)
)

# Create a tensor of inputs and set requires_grad=True
inputs = torch.randn(3, 5, requires_grad=True)

# Compute the output of the model using the input tensor
output = model(inputs)

# Compute the analytical gradients of the output with respect to the input tensor
analytical_grads = torch.autograd.grad(output, inputs)

# Compute the finite difference gradients of the output with respect to the input tensor
finite_diff_grads = torch.autograd.finite_diff(output, inputs)

# Compare the analytical and finite difference gradients
assert torch.allclose(analytical_grads, finite_diff_grads, atol=1e-4)
