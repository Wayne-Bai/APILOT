import torch
import torch.nn as nn
import torch.nn.functional as F

class ChannelDropout(nn.Module):
    def __init__(self, p=0.5):
        super(ChannelDropout, self).__init__()
        self.p = p

    def forward(self, x):
        if not self.training or self.p == 0:
            return x
        
        batch_size, num_channels, height, width = x.size()
        mask = torch.bernoulli(torch.full((batch_size, num_channels, 1, 1), 1 - self.p, device=x.device))
        return x * mask

# Example usage:
# model = nn.Sequential(
#     nn.Conv2d(3, 16, kernel_size=3, stride=1, padding=1),
#     ChannelDropout(p=0.5),
#     nn.ReLU(),
#     nn.MaxPool2d(kernel_size=2, stride=2)
# )
