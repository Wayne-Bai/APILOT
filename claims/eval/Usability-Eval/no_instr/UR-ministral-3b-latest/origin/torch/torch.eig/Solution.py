import torch

def compute_eigenvalues_decomposition(A):
    # Ensure input is a tensor and a square matrix
    assert A.is_complex() == False
    assert A.shape == (A.shape[0], A.shape[1])

    # Compute the eigenvalue decomposition using torch.bmesh
    e, v = torch.bmesh(A)

    # Sort values
    idcs = torch.sqrt(torch.abs(e)).sort()
    e = e[idcs.index]

    # Reorder the matrix v to match changed ordering
    v = v[:, idcs.index]

    return e, v

# Example usage
A = torch.tensor([[1, 2], [3, 4]])
eigenvalues, eigenvectors = compute_eigenvalues_decomposition(A)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:", eigenvectors)
