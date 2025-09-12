import torch
import torch.nn as nn
import torch.nn.functional as F

class RandomChannelErasing(nn.Module):
    def __init__(self, p=0.5, mean=0):
        super(RandomChannelErasing, self).__init__()
        self.p = p
        self.mean = mean

    def forward(self, x):
        if not self.training:
            return x

        channel_count = x.size(1)
        mask = torch.bernoulli(self.p * torch.ones(channel_count))
        mask = mask.bool()
        x[:, mask, ...] = self.mean
        return x
