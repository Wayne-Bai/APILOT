import torch
import torch.nn as nn

class GroupNorm(nn.Module):
    def __init__(self, num_groups, affine=True):
        super(GroupNorm, self).__init__()
        self.num_groups = num_groups
        self.affine = affine
        if affine:
            self.weight = nn.Parameter(torch.ones(1, num_groups, 1))
            self.bias = nn.Parameter(torch.zeros(1, num_groups, 1))

    def forward(self, x):
        N, C, H, W = x.size()
        assert C % self.num_groups == 0, "Number of groups should divide the input size."
        group_size = C // self.num_groups

        # Flatten the input tensor
        x = x.view(N, self.num_groups, group_size, H, W)

        # Calculate the mean and variance along the group dimension
        mean = x.mean(dim=2, keepdim=True)
        var = x.var(dim=2, keepdim=True)

        # Normalize the input tensor
        x = (x - mean) / torch.sqrt(var + 1e-5)

        # Apply affine transformation if enabled
        if self.affine:
            x = x * self.weight.expand_as(x) + self.bias.expand_as(x)

        # Reshape the input tensor back to its original shape
        x = x.view(N, C, H, W)

        return x
