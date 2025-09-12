import torch
import torch.nn as nn

class GroupNormLayer(nn.Module):
    def __init__(self, num_channels, num_groups):
        super(GroupNormLayer, self).__init__()
        self.group_norm = nn.GroupNorm(num_groups, num_channels)

    def forward(self, input):
        return self.group_norm(input)

# Test the GroupNormLayer
group_norm_layer = GroupNormLayer(64, 8)  # num_channels and num_groups
input_tensor = torch.randn(4, 64, 32, 32)  # Example input tensor with NCHW layout
output_tensor = group_norm_layer(input_tensor)  # Apply GroupNormLayer to input_tensor

print(output_tensor)
