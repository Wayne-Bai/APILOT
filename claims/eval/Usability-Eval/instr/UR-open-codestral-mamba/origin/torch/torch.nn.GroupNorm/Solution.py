import torch
import torch.nn as nn

class GroupNormalization(nn.Module):
    def __init__(self, num_features, num_groups=32, eps=1e-5, affine=True):
        super(GroupNormalization, self).__init__()
        self.num_features = num_features
        self.eps = eps
        self.num_groups = num_groups
        if affine:
            self.gamma = nn.Parameter(torch.ones(num_features))
            self.beta = nn.Parameter(torch.zeros(num_features))

    def forward(self, input):
        N, C, H, W = input.size()
        input = input.view(N, self.num_groups, -1)
        mean = input.mean(dim=2, keepdim=True)
        std = input.std(dim=2, keepdim=True)
        output = (input - mean) / (std + self.eps)
        output = output.view(N, C, H, W)
        if hasattr(self, 'gamma') and hasattr(self, 'beta'):
            output = self.gamma.view(1, -1, 1) * output + self.beta.view(1, -1, 1)
        return output

# Usage
input_tensor = torch.randn(32, 128, 32, 32)
model = GroupNormalization(128)
output_tensor = model(input_tensor)
print(output_tensor.size())
