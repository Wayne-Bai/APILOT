import torch

def compute_eigenvalue_decomposition(matrix):
    """
    Computes the eigenvalue decomposition of a square matrix if it exists.

    Args:
    matrix (torch.Tensor): A square matrix.

    Returns:
    eigenvalues (torch.Tensor): The eigenvalues of the input matrix.
    eigenvectors (torch.Tensor): The eigenvectors of the input matrix.

    Raises:
    ValueError: If the input matrix is not a square matrix.
    """

    # Check if the matrix is a square matrix
    if matrix.shape[0]!= matrix.shape[1]:
        raise ValueError("Input matrix must be a square matrix")

    # Compute the eigenvalue decomposition
    eigenvalues, eigenvectors = torch.linalg.eigh(matrix)

    return eigenvalues, eigenvectors


# Example usage
matrix = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
eigenvalues, eigenvectors = compute_eigenvalue_decomposition(matrix)

print("Eigenvalues:")
print(eigenvalues)
print("Eigenvectors:")
print(eigenvectors)
