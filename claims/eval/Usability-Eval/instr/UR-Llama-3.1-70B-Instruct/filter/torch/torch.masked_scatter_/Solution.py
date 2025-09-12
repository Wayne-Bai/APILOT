import torch
import torch.nn.functional as F

# Define a tensor and a mask
tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
mask = torch.tensor([[True, False, True], [True, False, True]])
source = torch.tensor([[9, 8, 7], [6, 5, 4]])

# Copy elements from source to tensor where mask is True
tensor[mask] = source[mask]

print(tensor)
