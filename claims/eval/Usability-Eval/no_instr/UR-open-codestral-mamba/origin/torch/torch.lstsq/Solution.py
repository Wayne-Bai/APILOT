import torch

# Assuming we have the system Ax = y and we are looking to find x
# A is the coefficient matrix and y is the constant matrix.

# Create system of linear equations
A = torch.tensor([[3.0, 2.0], [1.0, 4.0], [5.0, 6.0]])
y = torch.tensor([9.0, 6.0, 16.0])

# Solve the least squares solution using torch.lstsq()
# Note: torch.lstsq() returns a namedtuple whose first element is the least squares solution.
solution, *_ = torch.lstsq(y, A)
print(solution)
