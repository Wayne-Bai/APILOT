import torch
import torch.nn.functional as F

class ZeroChannel(torch.nn.Module):
    def __init__(self, p=0.5):
        super().__init__()
        self.p = p

    def forward(self, x):
        mask = torch.bernoulli(torch.empty(x.shape[0], x.shape[1], 1, 1).fill_(self.p))
        return x * mask
