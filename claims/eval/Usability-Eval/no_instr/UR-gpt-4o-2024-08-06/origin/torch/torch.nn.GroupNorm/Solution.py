import torch
import torch.nn as nn

class MyModel(nn.Module):
    def __init__(self, num_channels, num_groups):
        super(MyModel, self).__init__()
        self.group_norm = nn.GroupNorm(num_groups, num_channels)

    def forward(self, x):
        # Apply group normalization
        x = self.group_norm(x)
        return x

# Example usage
if __name__ == "__main__":
    # Create a random tensor with shape (batch_size, num_channels, height, width)
    input_tensor = torch.randn(8, 16, 32, 32)  # Example size

    model = MyModel(num_channels=16, num_groups=4)
    output = model(input_tensor)

    print(output.shape)
