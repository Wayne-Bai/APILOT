import torch

class RandomChannelZero(torch.nn.Module):
    def __init__(self, p):
        super(RandomChannelZero, self).__init__()
        self.p = p

    def forward(self, x):
        batch_size, channels, height, width = x.size()
        for i in range(channels):
            if torch.rand(1) < self.p:
                x[:, i, :, :] = 0
        return x

# Usage
p = 0.5
model = RandomChannelZero(p)
input_tensor = torch.rand(16, 3, 64, 64)
output_tensor = model(input_tensor)
print(output_tensor)
