import torch
from torch import nn

class GroupNormModel(nn.Module):
    def __init__(self, num_groups, num_channels, eps=1e-5, affine=True):
        super(GroupNormModel, self).__init__()
        self.group_norm = nn.GroupNorm(num_groups, num_channels, eps=eps, affine=affine)

    def forward(self, x):
        return self.group_norm(x)

# Example usage:
# num_groups = 4
# num_channels = 16
# model = GroupNormModel(num_groups, num_channels)
# input_tensor = torch.randn(2, 16, 32, 32)  # Example input tensor
# output = model(input_tensor)
