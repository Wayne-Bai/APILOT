import torch

# Assuming A is a tensor of shape (m, n) and b is a tensor of shape (m,)
# representing the coefficients and constant terms of the system of equations,
# respectively.

# Compute the solution to the least squares problem
x = torch.lstsq(b, A)[0]

# x is the tensor of solution(s) to the system of equations.
