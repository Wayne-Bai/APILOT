import torch

# Create a tensor
tensor = torch.tensor([1.0, 2.0, 3.0])

# Detach the tensor from the graph
detached_tensor = tensor.detach_()

# Verify that the tensor is detached
assert detached_tensor.requires_grad is False, "The tensor is still connected to the graph"
