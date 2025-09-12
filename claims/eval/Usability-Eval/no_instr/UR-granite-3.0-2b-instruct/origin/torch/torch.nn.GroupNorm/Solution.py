import torch
import torch.nn as nn

class GroupNorm(nn.Module):
    def __init__(self, num_groups, num_features):
        super(GroupNorm, self).__init__()
        self.num_groups = num_groups
        self.num_features = num_features
        self.weight = nn.Parameter(torch.ones(num_groups, num_features))
        self.bias = nn.Parameter(torch.zeros(num_groups, num_features))

    def forward(self, x):
        x = x.view(x.size(0), self.num_groups, -1)
        x = x.transpose(1, 2).contiguous()
        x = x.view(x.size(0), -1, self.num_groups, x.size(3))
        x = x.transpose(2, 3).contiguous()
        x = x.view(x.size(0), -1, self.num_features)
        x = torch.matmul(self.weight, x)
        x = torch.add(x, self.bias)
        x = x.view(x.size(0), -1, self.num_features)
        x = x.transpose(1, 2).contiguous()
        x = x.view(x.size(0), self.num_features)
        return x
