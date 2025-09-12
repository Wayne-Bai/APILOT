import torch

# Create a square matrix
A = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Compute the eigenvalue decomposition
eigenvalues, eigenvectors = torch.eig(A)

# Print the eigenvalues and eigenvectors
print("Eigenvalues:")
print(eigenvalues)
print("Eigenvectors:")
print(eigenvectors)
