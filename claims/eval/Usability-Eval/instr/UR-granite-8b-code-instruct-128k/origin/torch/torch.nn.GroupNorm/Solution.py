import torch

# Assuming x is the input tensor
x = torch.randn(10, 32, 10, 10)

# Applying Group Normalization
gn = torch.nn.GroupNorm(num_groups=32, num_channels=32)
output = gn(x)
