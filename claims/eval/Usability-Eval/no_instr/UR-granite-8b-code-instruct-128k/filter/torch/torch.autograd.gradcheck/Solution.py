
import torch

# Create a tensor with requires_grad=True and random float values
x = torch.rand(3, 3, requires_grad=True)

# Define a function that computes the loss as a sum of squares of the tensor
def f(x):
    return torch.sum(x ** 2)

# Compute the gradient of the function wrt the tensor using autograd
x.grad = torch.autograd.grad(f(x), x)[0]

# Print the computed gradients
print(x.grad)
