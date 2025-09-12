
import torch

class GroupNorm(torch.nn.Module):
    def __init__(self, num_channels, num_groups=8):
        super().__init__()
        self.num_channels = num_channels
        self.num_groups = num_groups
        self.weight = torch.nn.Parameter(torch.randn(1, num_channels))
        self.bias = torch.nn.Parameter(torch.zeros(1, num_channels))
        
    def forward(self, x):
        N, C, H, W = x.size()
        x = x.view(-1, 8, -1, H, W) # group the input into groups
        mean = torch.mean(x, dim=2, keepdim=True)
        var = torch.var(x, dim=2, keepdim=True)
        normed = (x-mean) / torch.sqrt(var + 1e-5)
        out = self.weight * normed + self.bias
        return out
