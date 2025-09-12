import torch

# Define source and mask tensors
source = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
mask = torch.tensor([[True, False, True], [False, True, False], [True, False, True]])

# Copy elements from source to destination tensor at positions where mask is True
destination = source.clone()
destination[mask] = source[mask]

# Print the destination tensor
print(destination)
