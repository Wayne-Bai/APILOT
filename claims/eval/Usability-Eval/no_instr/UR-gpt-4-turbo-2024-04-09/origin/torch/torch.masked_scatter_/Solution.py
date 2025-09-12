import torch

# Example tensors
source = torch.tensor([1, 2, 3, 4, 5])
mask = torch.tensor([True, False, True, False, True])
target = torch.tensor([0, 0, 0, 0, 0])

# Copy elements from source to target where mask is true
target.masked_scatter_(mask, source)

print(target)
