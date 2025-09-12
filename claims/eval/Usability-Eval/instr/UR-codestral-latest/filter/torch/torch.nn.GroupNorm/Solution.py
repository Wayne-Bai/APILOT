import torch
import torch.nn as nn

class GroupNormalization(nn.Module):
    """
    Group Normalization layer
    """
    def __init__(self, num_channels, num_groups=32, eps=1e-5):
        super(GroupNormalization, self).__init__()
        self.num_channels = num_channels
        self.num_groups = num_groups
        self.eps = eps

        self.gamma = nn.Parameter(torch.ones(1, num_channels, 1, 1))
        self.beta = nn.Parameter(torch.zeros(1, num_channels, 1, 1))

    def forward(self, x):
        batch_size, num_channels, height, width = x.size()

        x = x.view(batch_size, self.num_groups, -1)
        mean = x.mean(-1, keepdim=True)
        std = x.std(-1, keepdim=True)
        x = (x - mean) / (std + self.eps)
        x = x.view(batch_size, num_channels, height, width)

        return self.gamma * x + self.beta
