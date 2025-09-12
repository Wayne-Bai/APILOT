
import torch

# Initialize the source and destination tensors
src = torch.rand(5, 3)
dst = torch.rand(5, 3)
mask = torch.tensor([[1, 0], [0, 0]])

# Copy elements from src to dst at positions where the mask is True
torch.masked_scatter_(src, mask, dst)
