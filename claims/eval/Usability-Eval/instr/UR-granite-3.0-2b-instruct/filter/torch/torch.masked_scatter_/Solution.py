import torch

# Assuming src and mask are your input tensors
src = torch.tensor([1, 2, 3, 4, 5])
mask = torch.tensor([True, False, True, True, False])

# Create a new tensor to store the result
result = torch.empty_like(src)

# Copy elements from src into result at positions where mask is True
result[mask] = src[mask]

print(result)
