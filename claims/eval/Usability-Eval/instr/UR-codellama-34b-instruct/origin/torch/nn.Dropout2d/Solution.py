
import torch
import torch.nn as nn
from torch.distributions import Bernoulli

class RandomChannelZeroOut(nn.Module):
    def __init__(self, p=0.5):
        super(RandomChannelZeroOut, self).__init__()
        self.p = p
    
    def forward(self, x):
        # Generate a binary mask for each channel
        mask = Bernoulli(torch.tensor([1 - self.p] * x.shape[0]))
        mask = torch.unsqueeze(mask, 1)
        
        # Randomly zero out entire channels
        output = x * mask
        
        return output
