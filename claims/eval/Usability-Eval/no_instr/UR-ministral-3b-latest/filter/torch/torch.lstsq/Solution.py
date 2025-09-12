import torch

# Define input parameters
A = torch.tensor([[3, 2, -1], [2, -2, 4], [-1, 0.5, -1]], requires_grad=True)
b = torch.tensor([1, 2, 3], requires_grad=True)

# Perform the least squares solution
x_opt = torch.linalg.inv(A.t().matmul(A)) @ A.t().matmul(b)
print("Optimal x:", x_opt)
