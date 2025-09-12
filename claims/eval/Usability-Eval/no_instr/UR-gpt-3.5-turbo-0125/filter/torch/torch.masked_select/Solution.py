
import torch

# Generate 1-D input tensor
input_tensor = torch.tensor([1, 2, 3, 4, 5, 6])

# Generate boolean mask
mask = torch.tensor([True, False, True, False, True, False])

# Index the input tensor using the mask
output_tensor = input_tensor[mask]

print(output_tensor)
