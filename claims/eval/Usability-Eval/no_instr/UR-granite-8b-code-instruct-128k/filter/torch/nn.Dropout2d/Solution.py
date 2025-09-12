
import torch

class RandomChannelZeroOut(torch.nn.Module):
    def __init__(self, p):
        super(RandomChannelZeroOut, self).__init__()
        self.p = p

    def forward(self, x):
        if self.training:
            mask = torch.bernoulli(torch.ones_like(x) * self.p).cuda()
            return x * mask
        else:
            return x
