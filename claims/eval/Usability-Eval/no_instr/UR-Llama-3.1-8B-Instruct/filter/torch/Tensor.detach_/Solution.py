# Importing required modules from torch
import torch

# Creating a tensor
tensor = torch.tensor([1, 2, 3], requires_grad=True)

# Detaching the tensor from the graph that created it
detached_tensor = tensor.detach()

print(detached_tensor)
print(detached_tensor.requires_grad)  # Output: False
