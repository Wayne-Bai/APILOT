import torch

def compute_rank(matrix):
    # Compute the singular value decomposition (SVD) of the matrix
    u, s, vh = torch.svd(matrix)

    # The numerical rank of a matrix is equal to the number of non-zero singular values
    rank = torch.sum(s > 1e-10)

    return rank

# Example usage:
matrix = torch.rand(5, 5)  # Replace this with your matrix
print("Numerical rank of the matrix:", compute_rank(matrix))
