import torch
import torch.nn as nn

class GroupNorm(nn.Module):
    def __init__(self, num_groups, num_channels, eps=1e-5):
        super(GroupNorm, self).__init__()
        self.num_groups = num_groups
        self.num_channels = num_channels
        self.eps = eps
        self.weight = nn.Parameter(torch.ones(1, num_channels, 1, 1))
        self.bias = nn.Parameter(torch.zeros(1, num_channels, 1, 1))

    def forward(self, x):
        N, C, H, W = x.size()
        assert C % self.num_groups == 0
        group_size = C // self.num_groups
        x = x.view(N, self.num_groups, group_size, H, W)
        mean = x.mean(dim=[2, 3, 4], keepdim=True)
        var = x.var(dim=[2, 3, 4], keepdim=True)
        x = (x - mean) / torch.sqrt(var + self.eps)
        x = x * self.weight.expand(N, self.num_groups, group_size, H, W) + self.bias.expand(N, self.num_groups, group_size, H, W)
        x = x.view(N, C, H, W)
        return x
