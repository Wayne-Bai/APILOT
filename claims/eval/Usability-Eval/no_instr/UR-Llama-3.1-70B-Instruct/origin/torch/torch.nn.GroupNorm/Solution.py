import torch
import torch.nn as nn
import torch.nn.functional as F

class GroupNormalization(nn.Module):
    def __init__(self, num_groups, num_channels, eps=1e-5, affine=True):
        super(GroupNormalization, self).__init__()
        self.num_groups = num_groups
        self.num_channels = num_channels
        self.eps = eps
        self.affine = affine

        if self.affine:
            self.weight = nn.Parameter(torch.Tensor(num_channels))
            self.bias = nn.Parameter(torch.Tensor(num_channels))
            self.reset_parameters()

    def reset_parameters(self):
        if self.affine:
            nn.init.ones_(self.weight)
            nn.init.zeros_(self.bias)

    def forward(self, x):
        B, C, H, W = x.size()
        if self.num_channels % self.num_groups!= 0:
            raise ValueError('num_channels must be divisible by num_groups')

        x = x.view(B, self.num_groups, -1)
        mean = x.mean(-1, keepdim=True)
        var = x.var(-1, keepdim=True)

        x = (x - mean) / torch.sqrt(var + self.eps)
        x = x.view(B, C, H, W)

        if self.affine:
            x = x * self.weight.view(1, C, 1, 1) + self.bias.view(1, C, 1, 1)

        return x

# Example usage:
if __name__ == "__main__":
    batch_size, num_channels, height, width = 2, 16, 32, 32
    inputs = torch.randn(batch_size, num_channels, height, width)

    group_norm = GroupNormalization(num_groups=2, num_channels=num_channels)
    output = group_norm(inputs)
    print(output.shape)
