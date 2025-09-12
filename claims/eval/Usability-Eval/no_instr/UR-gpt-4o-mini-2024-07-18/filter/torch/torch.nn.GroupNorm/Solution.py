import torch
import torch.nn as nn

class GroupNormModel(nn.Module):
    def __init__(self, num_groups, num_features):
        super(GroupNormModel, self).__init__()
        self.group_norm = nn.GroupNorm(num_groups, num_features)

    def forward(self, x):
        return self.group_norm(x)

# Example usage:
if __name__ == "__main__":
    num_groups = 4
    num_features = 16
    batch_size = 8
    height, width = 32, 32
    
    # Create a random input tensor
    input_tensor = torch.randn(batch_size, num_features, height, width)
    
    # Initialize the model
    model = GroupNormModel(num_groups, num_features)
    
    # Forward pass
    output = model(input_tensor)
    print(output.shape)
