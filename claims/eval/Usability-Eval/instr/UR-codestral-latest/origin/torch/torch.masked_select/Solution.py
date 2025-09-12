import torch

# Assuming we have an input tensor and a boolean mask
input_tensor = torch.tensor([1, 2, 3, 4, 5])
mask = torch.tensor([True, False, True, False, True], dtype=torch.bool)

# Use the mask to index the input tensor
result = input_tensor[mask]
