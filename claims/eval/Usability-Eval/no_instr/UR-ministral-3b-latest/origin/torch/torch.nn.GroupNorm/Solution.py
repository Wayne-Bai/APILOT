import torch
from torch import nn
class GroupNorm(nn.Module):
    def __init__(self, num_groups, num_channels, epsilon=1e-5):
        super(GroupNorm, self).__init__()
        self.num_groups = num_groups
        self.num_channels = num_channels
        self.epsilon = epsilon

        self.gamma = nn.Parameter(torch.ones(1, num_channels))
        self.beta = nn.Parameter(torch.zeros(1, num_channels))

    def forward(self, x):
        n, c, h, w = x.size()
        m = c // self.num_groups

        # Compute the means and variances for each group
        res = torch.zeros_like(x)
        means = torch.mean(x, dim=[2, 3], keepdim=True)
        vars = torch.var(x, dim=[2, 3], keepdim=True, unbiased=False)

        res += self.gamma * torch.sqrt((vars + self.epsilon)[:, None, None, None])
        res += self.beta * torch.ones_like(x, dtype=torch.float)

        # Apply Mean and GroupNorm to each group
        for i in range(n):
            for j in range(0, c, m):
                for k in range(1):
                    res[i][j*m:j*m+m, :, :, :] = res[i][j*m:j*m+m, :, :, :] - means[i, :self.num_groups*m+j*k]
                    res[i][j*m:j*m+m, :, :, :] = res[i][j*m:j*m+m, :, :, :] / torch.sqrt(vars[i, :self.num_groups*m+j*k] + self.epsilon)

        return res