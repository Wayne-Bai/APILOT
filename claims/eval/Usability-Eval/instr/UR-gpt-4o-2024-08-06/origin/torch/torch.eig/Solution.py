import torch

def compute_eigen_decomposition(matrix):
    """
    Computes the eigenvalue decomposition of a square matrix if it exists.

    Parameters:
        matrix (torch.Tensor): A square matrix.

    Returns:
        eigenvalues (torch.Tensor): The eigenvalues of the matrix.
        eigenvectors (torch.Tensor): The matrix of eigenvectors.
    """
    if matrix.size(0) != matrix.size(1):
        raise ValueError("The input matrix must be square.")

    eigenvalues, eigenvectors = torch.linalg.eig(matrix)

    # To return real eigenvalues and eigenvectors if the input is real
    if matrix.is_floating_point():
        eigenvalues = eigenvalues.real
        eigenvectors = eigenvectors.real

    return eigenvalues, eigenvectors

# Example usage:
if __name__ == "__main__":
    # Define a square matrix
    matrix = torch.tensor([[4.0, -2.0], [1.0, 1.0]])

    eigenvalues, eigenvectors = compute_eigen_decomposition(matrix)

    print("Eigenvalues:\n", eigenvalues)
    print("Eigenvectors:\n", eigenvectors)
