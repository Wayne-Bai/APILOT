import torch

# Create a tensor
tensor = torch.tensor([1.0, 2.0, 3.0])

# Detach the tensor from the graph
detached_tensor = tensor.detach()

# Check if the tensor is a leaf node
assert detached_tensor.is_leaf
