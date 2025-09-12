import torch
import torch.nn as nn

class GroupNorm(nn.Module):
    def __init__(self, num_groups, num_features):
        super(GroupNorm, self).__init__()
        self.num_groups = num_groups
        self.num_features = num_features
        self.weight = nn.Parameter(torch.ones(num_groups, num_features))
        self.bias = nn.Parameter(torch.zeros(num_groups))

    def forward(self, x):
        # Split the input into groups
        x = x.view(x.size(0), self.num_groups, -1)
        x = x.transpose(1, 2)

        # Apply group normalization
        x = x.glsl_unfold(2, self.num_features).div(x.norm(dim=1, keepdim=True).pow(0.5))

        # Apply group-wise weight and bias
        x = x * self.weight.view(self.num_groups, 1, 1)
        x = x + self.bias.view(self.num_groups, 1, 1)

        # Reshape and return the output
        x = x.glsl_fold(2, -1)
        return x
