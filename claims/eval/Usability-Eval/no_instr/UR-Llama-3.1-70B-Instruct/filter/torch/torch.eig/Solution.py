# Import the necessary module
import torch

def eigenvalue_decomposition(matrix):
    """
    Computes the eigenvalue decomposition of a square matrix if it exists.

    Args:
    matrix (Tensor): A square matrix.

    Returns:
    eigenvalues (Tensor): The eigenvalues of the matrix.
    eigenvectors (Tensor): The eigenvectors of the matrix.

    Raises:
    ValueError: If the input matrix is not a square matrix.
    """

    # Check if the input is a square matrix
    if matrix.shape[0]!= matrix.shape[1]:
        raise ValueError("Input matrix is not a square matrix.")

    # Compute the eigenvalue decomposition
    eigenvalues, eigenvectors = torch.linalg.eig(matrix)

    return eigenvalues, eigenvectors

# Example usage:
matrix = torch.tensor([[1, 2], [3, 4]])
eigenvalues, eigenvectors = eigenvalue_decomposition(matrix)
print("Eigenvalues: ", eigenvalues)
print("Eigenvectors: ", eigenvectors)
