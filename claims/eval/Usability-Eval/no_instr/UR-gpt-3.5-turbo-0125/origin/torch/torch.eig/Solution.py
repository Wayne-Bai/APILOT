
import torch

# Create a square matrix A
A = torch.tensor([[1., 2.], [2., 1.]])

# Compute the eigenvalue decomposition of matrix A
eigenvalues, eigenvectors = torch.eig(A, eigenvectors=True)

print("Eigenvalues:")
print(eigenvalues)

print("Eigenvectors:")
print(eigenvectors)
