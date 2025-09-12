
import torch

# Define the system of linear equations as matrices A and B
A = torch.tensor([[1., 2.], [3., 4.]])
B = torch.tensor([1., 2.])

# Calculate the least squares solution using torch.linalg.lstsq which is an updated version
X, _ = torch.linalg.lstsq(B, A)

print(X)
