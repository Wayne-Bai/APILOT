import torch
import torch.nn as nn
from torch.nn import GroupNorm

# Let's assume that we are passing a 3D tensor as input with shape (Batch Size, Number of Channels, Height, Width)
x = torch.randn(4, 32, 20, 20)

# Define the Group Normalization layer
group_norm = GroupNorm(num_groups=4, num_channels=32)

# Apply Group Normalization to the input tensor
x_gn = group_norm(x)
