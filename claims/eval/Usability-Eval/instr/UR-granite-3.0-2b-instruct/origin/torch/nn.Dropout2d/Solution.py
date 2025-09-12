import torch
import torch.nn as nn
import torch.nn.functional as F

class ChannelZeroing(nn.Module):
    def __init__(self, p):
        super(ChannelZeroing, self).__init__()
        self.p = p

    def forward(self, x):
        # Generate a Bernoulli distribution for each channel
        probs = torch.rand_like(x) < self.p
        # Zero out the channels based on the probabilities
        x[probs == True] = 0
        return x
