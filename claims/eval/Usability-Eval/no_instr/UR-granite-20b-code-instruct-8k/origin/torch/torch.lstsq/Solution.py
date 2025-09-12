import torch

# Define the coefficient matrix A and the dependent variable vector b
A = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = torch.tensor([10, 11, 12])

# Compute the least squares solution
x = torch.lstsq(b, A)[0]

print("The solution to the least squares problem is:", x)
