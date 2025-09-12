import torch

def compute_eigenvalue_decomposition(matrix):
    # Ensure the input is a square matrix
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("The input must be a square matrix.")

    # Compute eigenvalues and eigenvectors
    eigenvalues, eigenvectors = torch.eig(matrix, eigenvectors=True)

    return eigenvalues, eigenvectors

# Example usage
if __name__ == "__main__":
    A = torch.tensor([[4.0, -2.0], [1.0, 1.0]])
    eigenvalues, eigenvectors = compute_eigenvalue_decomposition(A)
    print("Eigenvalues:\n", eigenvalues)
    print("Eigenvectors:\n", eigenvectors)
