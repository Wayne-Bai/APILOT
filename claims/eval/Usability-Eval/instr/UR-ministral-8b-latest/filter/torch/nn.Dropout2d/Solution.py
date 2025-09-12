import torch
import torch.nn.functional as F

class RandomZeroout(torch.nn.Module):
    def __init__(self, p):
        super(RandomZeroout, self).__init__()
        self.p = p

    def forward(self, x):
        batch_size, channels, height, width = x.size()
        random_mask = torch.bernoulli(torch.ones((batch_size, channels))) < self.p
        zeroout_indices = torch.arange(channels).unsqueeze(0).expand((batch_size, channels))
        x[random_mask == 0].scatter_(2, zeroout_indices[random_mask == 0].unsqueeze(-1).unsqueeze(-1), 0)
        return x

# Usage example
p = 0.5
model = RandomZeroout(p)
input_tensor = torch.randn(8, 3, 224, 224)  # example input tensor with batch size 8, 3 channels, 224x224 spatial dimensions
output_tensor = model(input_tensor)
print(output_tensor)
