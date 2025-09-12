
import torch

# Create input tensor
input_tensor = torch.tensor([1, 2, 3, 4, 5])

# Set the min and max values for clamping
min_val = 2
max_val = 4

# Clamp the input tensor within the specified range
output_tensor = torch.clamp(input_tensor, min=min_val, max=max_val)

print(output_tensor)
