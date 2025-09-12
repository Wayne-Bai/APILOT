import torch

# Create a sample function with parameters as inputs and grad_outputs
def sample_function(inputs, grad_outputs):
    return torch.sum(inputs * grad_outputs)

# Create some sample inputs and grad_outputs
inputs = torch.rand(5, 5, requires_grad=True, dtype=torch.float32)
grad_outputs = torch.rand(5, 5, dtype=torch.float32)

# Forward pass
output = sample_function(inputs, grad_outputs)

# Backward pass
output.backward()

# Get the analytical gradient
analytical_grad = inputs.grad.clone()

# Compute gradients using finite differences
eps = 1e-6
inputs_perturb = inputs + eps
output_perturb = sample_function(inputs_perturb, grad_outputs)
finite_diff_grad = (output_perturb - output) / eps

# Compare the gradients
print("Analytical Gradient:\n", analytical_grad)
print("Finite Difference Gradient:\n", finite_diff_grad)
