import torch

# Define a simple function that takes in a tensor and returns a tensor
def simple_function(x):
    return torch.sin(x) * torch.cos(x)

# Create a tensor with requires_grad=True
x = torch.tensor([1.0], requires_grad=True, dtype=torch.float32)

# Compute the analytical gradient
y = simple_function(x)
y.backward()
analytical_gradient = x.grad

# Compute the finite difference gradient
finite_difference_gradient = torch.autograd.functional.finite_diff(simple_function, x, eps=1e-5)

# Check if the gradients match
assert torch.allclose(analytical_gradient, finite_difference_gradient), "Gradients do not match"
print("Gradients match")
