import torch

def compute_eigen_decomposition(matrix):
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("The input matrix must be square.")

    try:
        # Compute the eigenvalues and eigenvectors
        eigenvalues, eigenvectors = torch.linalg.eig(matrix)
        
        # torch.linalg.eig might return complex results even for real matrices,
        # hence we convert them back to real numbers if the imaginary part is negligible.
        if torch.is_complex(eigenvalues):
            eigenvalues = eigenvalues.real
        if torch.is_complex(eigenvectors):
            eigenvectors = eigenvectors.real

        return eigenvalues, eigenvectors
    except RuntimeError as error:
        raise RuntimeError("Failed to compute the eigenvalue decomposition: ", error)

# Example usage:
matrix = torch.tensor([[4.0, -2.0], [-2.0, 1.0]])
eigenvalues, eigenvectors = compute_eigen_decomposition(matrix)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)
