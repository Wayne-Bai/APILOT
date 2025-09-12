import torch

# Define the function for which we want to check the gradients
def my_function(x):
    return x**2 + 2*x + 1

# Generate a tensor with requires_grad=True
x = torch.tensor([1.0], requires_grad=True)

# Compute the gradients using small finite differences
finite_diff_grad = torch.autograd.grad(my_function(x), x, create_graph=True)[0]

# Compute the gradients using autograd
autograd_grad = torch.autograd.grad(my_function(x), x)[0]

# Check if the gradients computed via small finite differences match the analytical gradients computed via autograd
grad_match = torch.allclose(finite_diff_grad, autograd_grad)

print(grad_match)
