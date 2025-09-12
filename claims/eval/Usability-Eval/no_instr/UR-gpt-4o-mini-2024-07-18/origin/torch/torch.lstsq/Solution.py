import torch

# Example: Solving the least squares problem Ax = b

# Define matrix A and vector b
A = torch.tensor([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
b = torch.tensor([7.0, 8.0, 9.0])

# Compute the pseudo-inverse of A
A_pseudo_inv = torch.linalg.pinv(A)

# Compute the least squares solution
x = A_pseudo_inv @ b

print("Least squares solution x:", x)
