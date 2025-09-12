
import torch
import torch.nn as nn
import torch.nn.functional as F

class GroupNorm2d(nn.Module):
    def __init__(self, num_groups, num_channels, eps=1e-5, affine=True):
        super(GroupNorm2d, self).__init__()
        self.num_groups = num_groups
        self.num_channels = num_channels
        self.eps = eps
        self.affine = affine

        if self.affine:
            self.weight = nn.Parameter(torch.Tensor(1, num_channels, 1, 1))
            self.bias = nn.Parameter(torch.Tensor(1, num_channels, 1, 1))
        else:
            self.register_parameter('weight', None)
            self.register_parameter('bias', None)

        self.reset_parameters()

    def reset_parameters(self):
        if self.affine:
            nn.init.ones_(self.weight)
            nn.init.zeros_(self.bias)

    def forward(self, x):
        N, C, H, W = x.size()
        G = self.num_groups
        assert C % G == 0, "Number of channels must be divisible by the number of groups."

        x = x.view(N, G, -1)

        mean = x.mean(dim=-1, keepdim=True)
        var = x.var(dim=-1, unbiased=False, keepdim=True)

        x = (x - mean) / torch.sqrt(var + self.eps)

        x = x.view(N, C, H, W)

        if self.affine:
            x = x * self.weight + self.bias

        return x
