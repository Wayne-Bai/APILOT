import torch

# Define the system of linear equations
A = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 10]])
B = torch.tensor([1, 2, 3])

# Solve the system of linear equations
X, residuals, rank, s = torch.lstsq(B, A)

# Print the solution
print('Solution:', X)

# Print the residuals
print('Residuals:', residuals)

# Print the rank of the matrix
print('Rank:', rank)

# Print the singular values of the matrix
print('Singular values:', s)
