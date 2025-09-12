
import torch

def eigenvalue_decomposition(matrix):
    try:
        eigenvalues, eigenvectors = torch.eig(matrix, eigenvectors=True)
        return eigenvalues, eigenvectors
    except RuntimeError as e:
        return "Eigenvalue decomposition does not exist for the given matrix."

# Example Usage
matrix = torch.tensor([[1., 2., 3.],
                        [4., 5., 6.],
                        [7., 8., 9.]])

eigenvalues, eigenvectors = eigenvalue_decomposition(matrix)
print("Eigenvalues:")
print(eigenvalues)
print("Eigenvectors:")
print(eigenvectors)
