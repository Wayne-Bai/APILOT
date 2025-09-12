import torch

# Define some example tensors
a = torch.randn(3, requires_grad=True)
b = torch.randn(3, requires_grad=True)

# Define a simple computation
c = a + b
d = c * 2

# Backpropagate to compute gradients
d.backward(torch.ones_like(d))

# Compute the sum of gradients with respect to graph leaves
grad_sum = a.grad + b.grad

print("Sum of gradients:", grad_sum)
