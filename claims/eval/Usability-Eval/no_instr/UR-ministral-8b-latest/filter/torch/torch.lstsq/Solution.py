import torch

# Assuming we have two lists A and B
A = torch.tensor([[3.0, -0.5], [5.0, 2.0]], dtype=torch.float32)
B = torch.tensor([5.0, 10.0], dtype=torch.float32)

# Compute the least squares solution using torch's QR decomposition
Q, R = torch.qr(A)
X = torch.linalg.solve_triangular(R, torch.linalg.solve_triangular(Q, torch.ones_like(R)))
print(X)
