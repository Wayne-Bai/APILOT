import torch

def compute_rank(matrix):
    # Compute the singular value decomposition (SVD) of the matrix
    U, S, V = torch.svd(matrix)

    # The rank of the matrix is the number of non-zero singular values
    rank = torch.sum(S > 1e-6)

    return rank
