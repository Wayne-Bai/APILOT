
import torch

# Create source, mask, and self tensors
source = torch.tensor([1, 2, 3, 4, 5])
mask = torch.tensor([1, 0, 1, 0, 1], dtype=torch.bool)
self_tensor = torch.zeros_like(source)

# Update self tensor using mask and source
self_tensor[mask] = source[mask]

print(self_tensor)
