import torch
import torch.nn as nn
import torch.nn.functional as F

class RandomZeroChannel(nn.Module):
    def __init__(self, p):
        super(RandomZeroChannel, self).__init__()
        self.p = p

    def forward(self, x):
        # x is a tensor of shape (batch_size, channels, height, width)
        # Compute a binary mask for each channel
        mask = torch.bernoulli(x.new_full((x.size(0), x.size(1), x.size(2), x.size(3)), 0.5)).float()

        # Multiply the input tensor by the mask to zero out the channels
        x = x * mask

        return x
