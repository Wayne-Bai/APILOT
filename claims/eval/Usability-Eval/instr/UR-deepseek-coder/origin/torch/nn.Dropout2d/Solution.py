import torch
import torch.nn as nn

class ChannelDropout(nn.Module):
    def __init__(self, p=0.5):
        super(ChannelDropout, self).__init__()
        self.p = p

    def forward(self, x):
        if not self.training:
            return x
        
        batch_size, num_channels, height, width = x.size()
        mask = torch.bernoulli(torch.full((batch_size, num_channels, 1, 1), 1 - self.p, device=x.device))
        return x * mask

# Example usage:
# model = nn.Sequential(
#     nn.Conv2d(3, 16, 3, 1, 1),
#     ChannelDropout(p=0.5),
#     nn.ReLU(),
#     nn.Conv2d(16, 32, 3, 1, 1),
#     ChannelDropout(p=0.5),
#     nn.ReLU(),
#     nn.AdaptiveAvgPool2d(1),
#     nn.Flatten(),
#     nn.Linear(32, 10)
# )
