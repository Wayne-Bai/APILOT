
import torch
import torch.nn as nn

# Define a GroupNorm class that inherits nn.Module
class GroupNorm(nn.Module):
    def __init__(self, num_groups, num_features, eps=1e-5, affine=True):
        super(GroupNorm, self).__init__()
        self.num_groups = num_groups
        self.num_features = num_features
        self.eps = eps
        self.affine = affine

        if self.affine:
            self.weight = nn.Parameter(torch.Tensor(num_features))
            self.bias = nn.Parameter(torch.Tensor(num_features))
        else:
            self.register_parameter('weight', None)
            self.register_parameter('bias', None)

        self.reset_parameters()

    def reset_parameters(self):
        if self.affine:
            nn.init.ones_(self.weight)
            nn.init.zeros_(self.bias)

    def forward(self, x):
        # Reshape x to shape (B, G, C//G, H, W) for group normalization
        B, C, H, W = x.size()
        assert C % self.num_groups == 0
        x = x.view(B, self.num_groups, -1, H, W)

        # Calculate group mean and var
        mean = x.mean(dim=[2, 3, 4], keepdim=True)
        var = x.var(dim=[2, 3, 4], unbiased=False, keepdim=True)

        # Normalize x
        x = (x - mean) / torch.sqrt(var + self.eps)

        # Reshape x back to original shape
        x = x.view(B, C, H, W)

        # Apply affine transformation if self.affine is True
        if self.affine:
            x = x * self.weight.view(1, -1, 1, 1) + self.bias.view(1, -1, 1, 1)

        return x
