import torch

def numerical_rank(matrix):
    # Compute the singular value decomposition of the matrix
    U, S, V = torch.svd(matrix)

    # The numerical rank is the number of singular values that are greater than a certain threshold
    threshold = 1e-10
    rank = sum(S > threshold)

    return rank
