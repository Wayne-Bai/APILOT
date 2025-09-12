import torch
import torch.nn as nn

class GroupNormalization(nn.Module):
    def __init__(self, num_groups, num_channels, eps=1e-5, affine=True):
        super(GroupNormalization, self).__init__()
        self.num_groups = num_groups
        self.num_channels = num_channels
        self.eps = eps
        self.affine = affine
        
        if self.num_channels % self.num_groups != 0:
            raise ValueError(f"num_channels should be divisible by num_groups, got num_channels={num_channels} and num_groups={num_groups}")
        
        if self.affine:
            self.weight = nn.Parameter(torch.ones(num_channels))
            self.bias = nn.Parameter(torch.zeros(num_channels))
        else:
            self.weight = None
            self.bias = None
    
    def forward(self, x):
        N, C, *dims = x.size()
        G = self.num_groups
        assert C % G == 0, "num_channels should be divisible by num_groups"
        x = x.view(N, G, -1)
        
        mean = x.mean(dim=-1, keepdim=True)
        var = x.var(dim=-1, unbiased=False, keepdim=True)
        
        x = (x - mean) / (var + self.eps).sqrt()
        x = x.view(N, C, *dims)
        
        if self.affine:
            x = self.weight.view(1, C, *([1] * (len(dims)))) * x + self.bias.view(1, C, *([1] * (len(dims))))
        
        return x

# Example usage:
# Create a GroupNormalization layer with 2 groups and 6 channels
gn = GroupNormalization(num_groups=2, num_channels=6)

# Create a dummy input tensor with shape (batch_size=2, num_channels=6, height=4, width=4)
input_tensor = torch.randn(2, 6, 4, 4)

# Apply Group Normalization
output_tensor = gn(input_tensor)
