import torch
import torch.nn as nn

class RandomChannelZeroout(nn.Module):
    def __init__(self, probability: float):
        super(RandomChannelZeroout, self).__init__()
        self.probability = probability

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        if not self.training:
            return x  # Do not apply when not in training mode
        # Create a mask to randomly zero out channels
        mask = torch.bernoulli(torch.full((x.shape[1],), 1 - self.probability)).unsqueeze(1).expand_as(x)
        return x * mask

# Example usage
if __name__ == "__main__":
    layer = RandomChannelZeroout(probability=0.3)
    layer.train()  # Set the layer to training mode
    input_tensor = torch.randn(2, 3, 4, 4)  # Example input: batch of 2, 3 channels, 4x4 feature maps
    output_tensor = layer(input_tensor)
    print(output_tensor)
