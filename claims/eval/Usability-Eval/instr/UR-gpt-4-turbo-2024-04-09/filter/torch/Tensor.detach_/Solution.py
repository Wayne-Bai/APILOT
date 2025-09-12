import torch

# Create a tensor that is part of a computation graph
x = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)
y = x * 2

# Detach the tensor from the graph
detached_x = y.detach()

print("Original x:", x)
print("Detached x:", detached_x)
