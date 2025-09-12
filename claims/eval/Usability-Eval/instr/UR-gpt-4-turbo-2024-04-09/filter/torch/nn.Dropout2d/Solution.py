import torch
import torch.nn as nn

class RandomChannelZeroOut(nn.Module):
    def __init__(self, p=0.5):
        super(RandomChannelZeroOut, self).__init__()
        if p < 0 or p > 1:
            raise ValueError("p must be in range [0, 1]")
        self.p = p

    def forward(self, x):
        if self.training:
            batch_size, num_channels, _, _ = x.size()
            # Sample mask: Bernoulli distribution (1-p means keep, p means zero out)
            mask = torch.bernoulli((1 - self.p) * torch.ones(num_channels)).unsqueeze(0).unsqueeze(2).unsqueeze(3)
            mask = mask.expand(batch_size, num_channels, x.size(2), x.size(3))
            return x * mask.to(x.device)
        else:
            return x

# Example usage
if __name__ == '__main__':
    torch.manual_seed(42)  # For reproducibility
    model = RandomChannelZeroOut(p=0.3)  # 30% chance to zero out each channel
    model.train()  # Enable training mode
    input_tensor = torch.randn(1, 5, 10, 10)  # Example input: (batch, channels, height, width)
    output = model(input_tensor)
    print(output)
