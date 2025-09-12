import torch

# Your input tensor
input_tensor = torch.randn(3, 5)  # This is just a random tensor for example

# Your minimum and maximum values
min_val = 0.0
max_val = 1.0

# Clamp all elements in input into the range [ min, max ]
clamped_tensor = torch.clamp(input_tensor, min=min_val, max=max_val)

print(clamped_tensor)
