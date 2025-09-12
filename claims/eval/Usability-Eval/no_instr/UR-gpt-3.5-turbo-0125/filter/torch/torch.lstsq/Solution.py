
import torch

# Generate random data for the linear system
A = torch.randn(3, 3)
b = torch.randn(3)

# Compute the least squares solution
x, _ = torch.lstsq(b.unsqueeze(1), A)

print(x)
