import torch
import torch.nn as nn

class RandomZeroOutChannels(nn.Module):
    def __init__(self, p):
        super(RandomZeroOutChannels, self).__init__()
        self.p = p  # Probability of zeroing out a channel

    def forward(self, input_tensor):
        # Number of channels in the input tensor
        num_channels = input_tensor.size(1)

        # Generate Bernoulli samples for each channel
        masks = torch.bernoulli(torch.tensor([self.p] * num_channels))

        # Zero out the entire channel if the mask is True
        output_tensor = input_tensor * masks.to(list(range(num_channels)))

        return output_tensor

# Example usage:
input_tensor = torch.randn(3, 4, 5)  # Example input tensor with batch size 3 and 4 features
p = 0.5  # Probability of zeroing out a channel

random_zero_out = RandomZeroOutChannels(p)
output_tensor = random_zero_out(input_tensor)

print(output_tensor)
