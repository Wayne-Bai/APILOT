
import torch
from torch.nn import GroupNorm2d

# Define the group normalization module
group_norm = GroupNorm2d(num_groups=3, num_features=16)

# Create a mini-batch of inputs
inputs = torch.randn(4, 3, 32, 32)

# Apply group normalization to the mini-batch of inputs
outputs = group_norm(inputs)
