import torch

# setup inputs (matrix and targets)
A = torch.tensor([[1., 1., 1.],
                  [1., 2., 3.],
                  [1., 3., 5.]])
B = torch.tensor([[2.],
                  [4.],
                  [6.]])

# use .solve() to compute the least squares solution
x = torch.linalg.solve(A.T @ A, A.T @ B)

print(x)
