# Import the necessary libraries
import torch
import torch.nn as nn
import torch.nn.functional as F

class CustomGroupNorm(nn.Module):
    """
    Applies Group Normalization over a mini-batch of inputs.
    """
    def __init__(self, num_groups=8, num_channels=None, eps=1e-5, affine=True):
        super(CustomGroupNorm, self).__init__()
        self.num_groups = num_groups
        self.num_channels = num_channels
        self.eps = eps
        self.affine = affine

        if self.affine:
            self.weight = nn.Parameter(torch.ones(num_channels))
            self.bias = nn.Parameter(torch.zeros(num_channels))

    def forward(self, x):
        N, C, H, W = x.size()
        if self.num_channels is None:
            self.num_channels = C

        # Reshape input for group normalization
        x = x.view(N, self.num_groups, C // self.num_groups, H, W)

        # Calculate mean and standard deviation per channel
        mean = x.mean(dim=[2, 3, 4], keepdim=True)
        var = x.var(dim=[2, 3, 4], keepdim=True)

        # Normalize the input
        x = (x - mean) / torch.sqrt(var + self.eps)

        # Reshape back to original shape
        x = x.view(N, C, H, W)

        # Apply learnable affine transformation (if applicable)
        if self.affine:
            x = x * self.weight[None, :, None, None] + self.bias[None, :, None, None]

        return x

# Example usage:
net = CustomGroupNorm(num_groups=8, num_channels=64)
input = torch.randn(1, 64, 32, 32)
output = net(input)
print(output.shape)
