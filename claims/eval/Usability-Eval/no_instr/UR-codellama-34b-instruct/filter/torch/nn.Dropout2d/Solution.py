
import torch
import torch.nn as nn
import torch.distributions as dist

class ChannelZeroing(nn.Module):
    def __init__(self, p=0.5):
        super().__init__()
        self.p = p
        
    def forward(self, x):
        if torch.rand(1) < self.p:
            n_channels = x.shape[1]
            channel_indices = torch.randperm(n_channels).to(x.device)
            zeroed_out_channels = channel_indices[:int(self.p * n_channels)]
            x[:, zeroed_out_channels, :] = 0
        return x
