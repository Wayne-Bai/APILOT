import torch

def eigendecomposition(matrix):
    try:
        eigenvalues, eigenvectors = torch.eig(matrix, eigenvectors=True)
        return eigenvalues, eigenvectors
    except RuntimeError:
        return "Eigendecomposition does not exist for this matrix."

# Example usage:
matrix = torch.tensor([[3.0, 2.0], [2.0, 3.0]])
print(eigendecomposition(matrix))
