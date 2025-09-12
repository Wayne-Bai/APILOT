import torch

# Create a random square matrix
matrix = torch.randn(5, 5)

# Compute the eigenvalues and eigenvectors
eigenvalues, eigenvectors = torch.eig(matrix, eigenvectors=True)

print('Eigenvalues:', eigenvalues)
print('Eigenvectors:', eigenvectors)
