import torch

def eigenvalue_decomposition(matrix):
    if not isinstance(matrix, torch.Tensor):
        raise ValueError("Input must be a PyTorch tensor.")
    
    if matrix.dim() != 2 or matrix.size(0) != matrix.size(1):
        raise ValueError("Input must be a square matrix.")
    
    # Computing the eigenvalue decomposition
    eigenvalues, eigenvectors = torch.eig(matrix, eigenvectors=True)

    return eigenvalues, eigenvectors

# Example usage
matrix = torch.tensor([[4.0, 1.0], [2.0, 3.0]])
eigenvalues, eigenvectors = eigenvalue_decomposition(matrix)

print("Eigenvalues:\n", eigenvalues)
print("Eigenvectors:\n", eigenvectors)
