import torch

# Example tensor
tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.float)

# Mask tensor. Note the mask should be broadcastable to the tensor
mask = torch.tensor([[True, False, True], [False, True, False], [True, True, False]])

# The value to use for filling
fill_value = 0.0

# Filling elements of tensor where mask is True
tensor[mask] = fill_value

print(tensor)
