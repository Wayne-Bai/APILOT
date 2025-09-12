import torch
import torch.nn as nn

class GroupNorm(nn.Module):
    def __init__(self, num_groups, num_channels, eps=1e-5, affine=True):
        super(GroupNorm, self).__init__()
        self.num_groups = num_groups
        self.num_channels = num_channels
        self.eps = eps
        self.affine = affine
        if self.affine:
            self.weight = nn.Parameter(torch.ones(1, num_channels, 1, 1))
            self.bias = nn.Parameter(torch.zeros(1, num_channels, 1, 1))
        else:
            self.register_parameter('weight', None)
            self.register_parameter('bias', None)

    def forward(self, x):
        N, C, H, W = x.size()
        assert C % self.num_groups == 0, "Number of channels should be divisible by num_groups"
        
        x = x.view(N, self.num_groups, -1)
        mean = x.mean(dim=2, keepdim=True)
        var = x.var(dim=2, keepdim=True)
        x = (x - mean) / torch.sqrt(var + self.eps)
        x = x.view(N, C, H, W)
        
        if self.affine:
            x = self.weight * x + self.bias
        
        return x

# Example usage:
# model = GroupNorm(num_groups=4, num_channels=16)
# input_tensor = torch.randn(8, 16, 32, 32)
# output = model(input_tensor)
