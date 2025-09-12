import torch

# Generate some random coefficients for the coefficients matrix A and the target vector b
A = torch.randn(3, 4, requires_grad=True)
b = torch.randn(4, requires_grad=True)

# Compute the normal equation solution using torch.linalg (so as not to use outdated 'lstsq' API)
x = torch.linalg.solve(A, b)

print("Solution:", x)
