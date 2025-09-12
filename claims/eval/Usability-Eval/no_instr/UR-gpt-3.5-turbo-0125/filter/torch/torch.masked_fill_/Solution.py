
import torch

# Create a tensor
self_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])

# Create a mask with the same shape as self_tensor
mask = torch.tensor([[True, False, True], [False, True, False]])

# Fill elements of self_tensor with value (e.g., 0) where mask is True
value = 0
self_tensor[mask] = value

print(self_tensor)
