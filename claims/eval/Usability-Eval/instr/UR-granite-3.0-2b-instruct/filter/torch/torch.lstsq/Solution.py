import torch

# Define the coefficient matrix A and the target vector b
A = torch.tensor([[3., 2., -1.],
                  [2., -2., 4.],
                  [-1., 0.5, -1.]], dtype=torch.float32)

b = torch.tensor([1., -2., 0.], dtype=torch.float32)

# Compute the least squares solution using PyTorch's linalg.solve function
x = torch.linalg.solve(A, b)

print("The least squares solution is:", x)
