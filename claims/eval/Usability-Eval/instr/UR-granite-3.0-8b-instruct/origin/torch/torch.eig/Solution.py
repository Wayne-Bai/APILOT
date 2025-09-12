import torch

def eigen_decomposition(matrix):
    eigenvalues, eigenvectors = torch.eig(matrix)
    return eigenvalues, eigenvectors

# Example usage:
matrix = torch.tensor([[1, 2], [3, 4]])
eigenvalues, eigenvectors = eigen_decomposition(matrix)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)
