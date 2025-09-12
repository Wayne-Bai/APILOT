
import torch
import torch.nn.functional as F

class ZeroOutChannels(torch.nn.Module):
    def __init__(self, num_channels, p):
        super(ZeroOutChannels, self).__init__()
        self.num_channels = num_channels
        self.p = p

    def forward(self, x):
        if self.training:
            mask = (torch.rand(x.size(0), self.num_channels, 1, 1) > self.p).float().to(x.device)
            return x * mask
        else:
            return x
