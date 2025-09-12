import torch
import torch.nn as nn
import torch.nn.functional as F

class RandomChannelDropout(nn.Module):
    def __init__(self, p, inplace=False):
        super(RandomChannelDropout, self).__init__()
        self.p = p
        self.inplace = inplace
        self.bernoulli = None

    def forward(self, x):
        if self.bernoulli is None:
            self.bernoulli = torch.bernoulli(torch.ones_like(x[:, 0, 0, 0], dtype=torch.float32) * self.p)
        zeros = torch.zeros_like(x)
        mask = torch.unsqueeze(torch.unsqueeze(torch.unsqueeze(self.bernoulli, 2), 3), 1)
        result = x * (1 - mask) + zeros * mask
        return result
