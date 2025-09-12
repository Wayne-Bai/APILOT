import torch
import torch.nn as nn

class GroupNorm(nn.Module):
    def __init__(self, num_channels, num_groups, epsilon=1e-5):
        super(GroupNorm, self).__init__()
        self.num_channels = num_channels
        self.num_groups = num_groups
        self.epsilon = epsilon

        self.weight = nn.Parameter(torch.ones(num_channels))
        self.bias = nn.Parameter(torch.zeros(num_channels))

    def forward(self, x):
        N, C, H, W = x.shape
        G = self.num_groups

        x_view = x.view(N, G, C // G, H, W)
        mean = x_view.mean(dim=[2, 3, 4], keepdim=True)
        mean = mean.view(N, G, 1, 1)

        var = torch.square(x_view - mean).sum(dim=[2, 3, 4], keepdim=True)
        var = var.mean(dim=0)

        norm = torch.sqrt(var + self.epsilon)
        normalized = (x_view - mean) / norm
        output = normalized.view(N, C, H, W) * self.weight.view(1, -1, 1, 1) + self.bias.view(1, C, 1, 1)

        return output

# Example usage
if __name__ == "__main__":
    model = GroupNorm(num_channels=3, num_groups=32)
    inputs = torch.randn(1, 3, 28, 28)
    output = model(inputs)
    print(output.shape)  # should output: torch.Size([1, 3, 28, 28])
