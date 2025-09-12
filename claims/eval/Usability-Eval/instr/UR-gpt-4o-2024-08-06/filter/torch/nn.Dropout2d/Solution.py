import torch
import torch.nn as nn
import torch.nn.functional as F

class ChannelDropout(nn.Module):
    def __init__(self, p=0.5):
        super(ChannelDropout, self).__init__()
        self.p = p

    def forward(self, x):
        if not self.training or self.p == 0.0:
            return x
        
        batch_size, num_channels, height, width = x.size()
        # Generate a mask from a Bernoulli distribution
        mask = torch.bernoulli(torch.empty(batch_size, num_channels, 1, 1, device=x.device).fill_(1 - self.p))
        # Multiply input tensor with mask to zero out channels
        mask = mask.expand_as(x)
        return x * mask

# Example usage
# model = ChannelDropout(p=0.3)
# output = model(input_tensor)
