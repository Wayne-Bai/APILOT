
import torch

# Create a tensor and add it to a graph
x = torch.tensor([1, 2, 3])
y = torch.randn(3)
z = x + y

# Detach the tensor from the graph
detached_x = torch.detach(x)

# Use the detached tensor in a new computation
w = detached_x * y
