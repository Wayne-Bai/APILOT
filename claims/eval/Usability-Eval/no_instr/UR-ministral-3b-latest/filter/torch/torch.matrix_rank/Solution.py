import torch

def compute_svd(matrix):
    # Get the SVD decomposition of the matrix
    U, s, Vt = torch.svd(matrix)

    # Compute the rank as the number of singular values greater than the threshold
    rank = (s > 1e-8).sum().item()

    return rank

# Example usage
matrix = torch.randn(10, 8)
rank = compute_svd(matrix)
print(f"The numerical rank of the matrix is: {rank}")
