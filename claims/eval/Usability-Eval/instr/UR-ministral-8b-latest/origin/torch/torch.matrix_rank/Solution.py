import torch

def numerical_rank(matrix):
    eigenvalues = torch.linalg.eigvals(matrix)
    return torch.count_nonzero(torch.abs(eigenvalues))  # Count the number of non-zero eigenvalues

# Example matrix
matrix = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
rank = numerical_rank(matrix)

print(f"The numerical rank of the given matrix is: {rank}")
