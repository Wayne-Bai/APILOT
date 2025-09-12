import torch
from torch.nn import GroupNorm

# Define the input tensor
input = torch.randn(10, 64, 100, 100)

# Define the GroupNorm layer with 8 groups
gn = GroupNorm(8, 64)

# Apply GroupNorm to the input tensor
output = gn(input)

# Print the output tensor
print(output)
