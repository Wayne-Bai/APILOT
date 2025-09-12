import torch
import torch.nn as nn
import torch.nn.functional as F

def drop_channels(x, p=0.5):
    if p == 0:
        return x
    mask = torch.zeros(x.size(1)).bernoulli_(1 - p)
    mask = mask.view(1, -1, 1, 1).expand_as(x)
    return x * mask

class YourModel(nn.Module):
    def __init__(self, drop_probability):
        super(YourModel, self).__init__()
        self.drop_probability = drop_probability

    def forward(self, x):
        x = drop_channels(x, self.drop_probability)
        # Rest of your model operations...
        return x
