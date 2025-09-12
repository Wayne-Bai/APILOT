import torch
import torch.nn as nn

class MyGroupNorm(nn.Module):
    def __init__(self, num_groups, num_channels, eps=1e-5):
        super(MyGroupNorm, self).__init__()
        self.group_norm = nn.GroupNorm(num_groups, num_channels, eps=eps)

    def forward(self, x):
        return self.group_norm(x)

# Example usage
num_groups = 4
num_channels = 32
input_tensor = torch.randn(8, 32, 100, 100)  # Example input (batch of 8 with 32 channels each of 100x100 size)

group_norm = MyGroupNorm(num_groups, num_channels)
output = group_norm(input_tensor)
