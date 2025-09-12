
import torch
import random

class RandomChannelZeroing(nn.Module):
    def __init__(self, p=0.5):
        super(RandomChannelZeroing, self).__init__()
        self.p = p

    def forward(self, x):
        # Get the number of channels in the input tensor
        n_channels = x.size(1)

        # Create a random mask with the same shape as the input tensor
        mask = torch.zeros_like(x).bernoulli_(p)

        # Zero out entire channels (2D feature maps) with probability p
        for i in range(n_channels):
            channel_mask = mask[:, i:i+1]
            x[..., i] = x[..., i] * channel_mask

        return x
