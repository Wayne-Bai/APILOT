
import torch
def matrix_rank(matrix):
    matrix_numpy = matrix.numpy()
    rank = np.linalg.matrix_rank(matrix_numpy)
    return rank
