
import torch

class RandomChannelZeroOut(nn.Module):
    def __init__(self, p):
        super(RandomChannelZeroOut, self).__init__()
        self.p = p
    
    def forward(self, x):
        if self.training:
            bernoulli = torch.distributions.Bernoulli(probs=self.p)
            random_tensor = bernoulli.sample(x.size())
            x = x * random_tensor
        return x
