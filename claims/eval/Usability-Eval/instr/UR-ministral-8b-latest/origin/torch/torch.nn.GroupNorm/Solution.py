import torch
import torch.nn as nn
import torch.nn.functional as F

class GroupNorm(nn.Module):
    def __init__(self, num_groups, num_channels, eps=1e-5):
        super(GroupNorm, self).__init__()
        self.num_groups = num_channels // num_groups
        self.gamma = nn.Parameter(torch.ones(num_channels))
        self.beta = nn.Parameter(torch.zeros(num_channels))
        self.eps = eps

    def forward(self, x):
        N = x.size(0)
        C = x.size(1)

        x = x.view(N, self.num_groups, C // self.num_groups, -1)
        mean = x.mean([-1, -2], keepdim=True)
        std = x.std([-1, -2], keepdim=True)
        x = (x - mean) / (std + self.eps)

        x = x.view(N, C, x.size(-1))
        return self.gamma * x + self.beta

# Usage
# Assume you have a mini-batch of inputs with shape (N, C, H, W)
N, C, H, W = 16, 32, 32, 32
x = torch.randn(N, C, H, W)

# Apply GroupNorm
num_groups = 8
group_norm = GroupNorm(num_groups, C)
y = group_norm(x)
print(y.shape)  # Output should be: torch.Size([16, 32, 32, 32])
