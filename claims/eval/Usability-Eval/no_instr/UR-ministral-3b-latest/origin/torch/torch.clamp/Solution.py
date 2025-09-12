import torch

# Sample input tensor
input_tensor = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])

# Define the minimum and maximum values
min_val = 0.0
max_val = 10.0

# Clamp all elements in the input tensor to the range [min, max]
clamped_tensor = torch.clamp(input_tensor, min=min_val, max=max_val)

print(clamped_tensor)
