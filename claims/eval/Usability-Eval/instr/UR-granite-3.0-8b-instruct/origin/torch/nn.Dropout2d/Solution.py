import torch
import torch.nn as nn
import torch.nn.functional as F

class RandomChannelOut(nn.Module):
    def __init__(self, p=0.5):
        super(RandomChannelOut, self).__init__()
        self.p = p

    def forward(self, x):
        if self.training:
            mask = torch.bernoulli(self.p * torch.ones_like(x))
            x = x * mask
        return x
