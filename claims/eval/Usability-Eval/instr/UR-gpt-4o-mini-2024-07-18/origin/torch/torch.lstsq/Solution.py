import torch

# Create a sample matrix A and vector b
A = torch.tensor([[2.0, 3.0], [1.0, 1.0], [4.0, 1.0]])
b = torch.tensor([5.0, 2.0, 7.0])

# Solve the least squares problem
x, _ = torch.linalg.lstsq(A, b)

print("The least squares solution is:", x)
