import torch
import numpy as np

class ChannelRandomZero(torch.nn.Module):
    def __init__(self, p):
        super().__init__()
        self.p = p

    def forward(self, x):
        probable_zero = np.random.rand(len(x.shape)) < self.p
        x = x * (1 - probable_zero.float().unsqueeze(-1) + 1e-6)  # Avoid overflow
        return x

# Example usage:
# model = ChannelRandomZero(p=0.3)
# x = torch.randn(8, 3, 128, 128)  # batch_size = 8, channels = 3, height = 128, width = 128
# y = model(x)
