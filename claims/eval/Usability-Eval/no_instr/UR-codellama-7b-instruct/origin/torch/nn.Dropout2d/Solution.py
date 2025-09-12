
import torch

class ZeroOutChannels(nn.Module):
    def __init__(self, channels, p=0.5):
        super().__init__()
        self.channels = channels
        self.p = p
    
    def forward(self, x):
        mask = torch.distributions.Bernoulli(probs=torch.full((1, self.channels), fill_value=self.p)).sample()
        return torch.mul(x, mask)
