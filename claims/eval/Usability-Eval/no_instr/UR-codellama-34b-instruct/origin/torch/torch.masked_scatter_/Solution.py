
import torch

# Define the source and mask tensors
source = torch.tensor([1, 2, 3])
mask = torch.tensor([True, False, True])

# Copy elements from source to self tensor at positions where mask is True
self_tensor = source[mask]
