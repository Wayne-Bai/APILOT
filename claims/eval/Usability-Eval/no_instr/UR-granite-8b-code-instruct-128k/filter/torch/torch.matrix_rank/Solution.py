import torch

def compute_numerical_rank(matrix):
    singular_values = torch.svd(matrix, compute_uv=False)
    rank = (singular_values > 1e-5).sum().item()
    return rank
