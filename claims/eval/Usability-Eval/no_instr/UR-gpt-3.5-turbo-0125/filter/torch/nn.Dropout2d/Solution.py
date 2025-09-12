
import torch
import torch.nn as nn

class ZeroOutChannels(nn.Module):
    def __init__(self, p):
        super(ZeroOutChannels, self).__init__()
        self.p = p

    def forward(self, x):
        if self.training:
            batch_size, num_channels, height, width = x.size()
            mask = torch.zeros(num_channels).bernoulli_(self.p).view(1, num_channels, 1, 1).expand_as(x)
            x = x * mask
        return x
