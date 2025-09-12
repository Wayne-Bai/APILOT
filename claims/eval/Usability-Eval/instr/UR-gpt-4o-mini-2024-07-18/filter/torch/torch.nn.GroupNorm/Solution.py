import torch
import torch.nn as nn

class GroupNormModel(nn.Module):
    def __init__(self, num_groups, num_channels):
        super(GroupNormModel, self).__init__()
        self.group_norm = nn.GroupNorm(num_groups, num_channels)

    def forward(self, x):
        return self.group_norm(x)

# Example usage:
if __name__ == "__main__":
    num_groups = 4
    num_channels = 8
    model = GroupNormModel(num_groups, num_channels)
    
    # Create a random tensor with shape (batch_size, num_channels, height, width)
    input_tensor = torch.randn(16, num_channels, 32, 32)  # Batch size of 16
    output = model(input_tensor)
    print(output.shape)
