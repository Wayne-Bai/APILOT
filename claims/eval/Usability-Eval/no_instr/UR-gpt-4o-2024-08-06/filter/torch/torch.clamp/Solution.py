import torch

# Define the input tensor
input_tensor = torch.tensor([0.5, 2.0, 3.5, 5.0, 7.5, 10.0])

# Define the min and max values for clamping
min_value = 3.0
max_value = 8.0

# Clamp the input tensor
clamped_tensor = torch.clamp(input_tensor, min=min_value, max=max_value)

# Print the result
print(clamped_tensor)
