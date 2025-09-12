import torch

def eigenvalue_decomposition(matrix):
    if matrix.size(0) != matrix.size(1):
        raise ValueError("Matrix must be square")
    
    eigenvalues, eigenvectors = torch.linalg.eig(matrix)
    return eigenvalues, eigenvectors

# Example usage
A = torch.tensor([[4.0, -2.0], [1.0, 1.0]], dtype=torch.float32)
eigenvalues, eigenvectors = eigenvalue_decomposition(A)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:", eigenvectors)
