import torch
import torch.nn as nn

class RandomChannelZeroOut(nn.Module):
    def __init__(self, p=0.5):
        super().__init__()
        if not (0 <= p <= 1):
            raise ValueError("Drop probability has to be between 0 and 1, but got {}".format(p))
        self.p = p

    def forward(self, x):
        if self.training:
            # Generate random mask, shape is (batch_size, channels, 1, 1) to broadcast across spatial dimensions
            batch_size, channels, _, _ = x.size()
            mask = torch.bernoulli((1 - self.p) * torch.ones(batch_size, channels, 1, 1, device=x.device))
            return x * mask
        return x

# Example usage:
# Assuming `x` is a batch of images with shape [batch size, channels, height, width]
# Initialize the module
# channel_zero_out = RandomChannelZeroOut(p=0.3)
# Output will have the same size as input `x` but with some channels zeroed out randomly.
