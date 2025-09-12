# Import necessary modules from PyTorch
import torch
import torch.nn as nn
import torch.nn.functional as F

# Define a Group Normalization layer
class GroupNormLayer(nn.Module):
    def __init__(self, num_groups, num_channels, eps=1e-5, momentum=0.1):
        """
        Initializes the Group Normalization layer.

        Args:
        - num_groups (int): Number of groups to split the channels into.
        - num_channels (int): Total number of input channels.
        - eps (float): Small value to prevent division by zero.
        - momentum (float): Momentum value for the running mean and variance.
        """
        super(GroupNormLayer, self).__init__()
        self.num_groups = num_groups
        self.eps = eps
        self.momentum = momentum
        self.GroupNorm = nn.GroupNorm(num_groups, num_channels, eps, momentum)

    def forward(self, x):
        """
        Applies Group Normalization over the input tensor.

        Args:
        - x (Tensor): Input tensor with shape (batch_size, num_channels, height, width).

        Returns:
        - Tensor: Normalized input tensor with shape (batch_size, num_channels, height, width).
        """
        return self.GroupNorm(x)


# Example usage:
if __name__ == "__main__":
    # Create a batch of random inputs with shape (2, 3, 4, 4)
    x = torch.randn(2, 3, 4, 4)

    # Create a Group Normalization layer with 3 groups and 3 channels
    group_norm_layer = GroupNormLayer(num_groups=3, num_channels=3)

    # Apply Group Normalization to the input batch
    normalized_x = group_norm_layer(x)

    print(normalized_x.shape)
