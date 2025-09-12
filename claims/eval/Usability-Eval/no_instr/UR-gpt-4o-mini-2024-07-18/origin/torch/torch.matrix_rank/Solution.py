import torch

def compute_numerical_rank(matrix, tol=None):
    if tol is None:
        tol = torch.max(matrix.shape) * torch.linalg.norm(matrix) * torch.finfo(matrix.dtype).eps
    # Compute singular values
    singular_values = torch.linalg.svd(matrix, compute_uv=False)
    # Count the number of singular values greater than the tolerance
    rank = (singular_values > tol).sum().item()
    return rank

# Example usage
A = torch.tensor([[1.0, 2.0], [2.0, 4.0], [3.0, 6.0]])
rank = compute_numerical_rank(A)
print(f"The numerical rank of the matrix is: {rank}")
