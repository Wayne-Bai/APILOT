
import torch

# Define some tensors
x = torch.tensor([2.0], requires_grad=True)
y = torch.tensor([3.0], requires_grad=True)

# Perform some operations
a = x * y
b = x + y

# Compute the sum of gradients with respect to graph leaves
torch.autograd.backward([a, b], torch.tensor([1.0]))
