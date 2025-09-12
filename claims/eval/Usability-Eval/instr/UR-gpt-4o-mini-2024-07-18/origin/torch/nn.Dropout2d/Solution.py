import torch
import torch.nn as nn

class RandomChannelZeroing(nn.Module):
    def __init__(self, p=0.5):
        super(RandomChannelZeroing, self).__init__()
        self.p = p

    def forward(self, x):
        # Get the number of channels
        batch_size, num_channels, height, width = x.size()
        
        # Sample from Bernoulli distribution
        mask = torch.bernoulli(torch.full((batch_size, num_channels, 1, 1), 1 - self.p)).to(x.device)

        # Zero out channels based on the mask
        x = x * mask
        
        return x

# Example usage
if __name__ == "__main__":
    model = RandomChannelZeroing(p=0.5)
    input_tensor = torch.randn(8, 3, 32, 32)  # Example input with batch_size=8, num_channels=3, height=32, width=32
    output_tensor = model(input_tensor)
    print(output_tensor)
