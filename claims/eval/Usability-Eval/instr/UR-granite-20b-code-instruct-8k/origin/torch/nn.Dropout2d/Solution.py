import torch

class RandomZeroout(nn.Module):
    def __init__(self, probability):
        super(RandomZeroout, self).__init__()
        self.probability = probability
    
    def forward(self, x):
        # Generate a random binary tensor with the same shape as x
        mask = torch.bernoulli(torch.ones_like(x) * self.probability)
        # Multiply x with the binary tensor to randomly zero out channels
        x = x * mask
        
        return x
