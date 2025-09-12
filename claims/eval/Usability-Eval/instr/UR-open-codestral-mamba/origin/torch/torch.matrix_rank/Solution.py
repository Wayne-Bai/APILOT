import torch

def compute_rank(matrix):
    # Convert the input to a tensor
    matrix_tensor = torch.tensor(matrix)

    # Compute the rank using torch.linalg.matrix_rank
    rank = torch.linalg.matrix_rank(matrix_tensor)

    return rank

# Usage
matrix = [[1, 2], [3, 4]]
rank = compute_rank(matrix)
print(f"Rank of the matrix: {rank}")
