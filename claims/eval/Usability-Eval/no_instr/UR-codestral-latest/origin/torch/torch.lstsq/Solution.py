import torch

# Assume A is a n x p matrix and b is a n x 1 vector
# The goal is to find x in A*x = b

A = torch.tensor([[3., 2.], [1., 1.]], dtype=torch.float32)
b = torch.tensor([[9.], [6.]], dtype=torch.float32)

# Computing the least squares solution
x, _ = torch.lstsq(b, A)

print("The solution is:", x)
