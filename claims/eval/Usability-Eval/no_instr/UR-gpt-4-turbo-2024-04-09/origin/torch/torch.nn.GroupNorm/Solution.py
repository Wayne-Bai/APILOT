import torch
import torch.nn as nn

# Define Group Normalization layer
class GroupNormLayer(nn.Module):
    def __init__(self, num_groups, num_channels):
        super(GroupNormLayer, self).__init__()
        self.group_norm = nn.GroupNorm(num_groups, num_channels)

    def forward(self, x):
        return self.group_norm(x)

# Example usage
if __name__ == "__main__":
    # Creating a tensor
    tensor = torch.randn(2, 8, 10, 10)  # For example, (batch size, channels, height, width)
    
    # Number of groups and number of channels
    num_groups = 4
    num_channels = 8  # Number of channels must be divisible by the number of groups

    # Create an instance of the GroupNorm layer
    group_norm_layer = GroupNormLayer(num_groups, num_channels)
    
    # Apply Group Normalization
    output = group_norm_layer(tensor)
    print(output)
