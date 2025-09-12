import torch

# Create a source tensor
source = torch.tensor([[1, 2, 3], [4, 5, 6]])

# Create a mask tensor
mask = torch.tensor([[True, False, True], [False, True, False]])

# Create a target tensor
target = torch.zeros(2, 3)

# Copy elements from source to target at positions where mask is True
target[mask] = source[mask]

print(target)
