import numpy as np

def zero_lower_k_diagonal(matrix, k):
    # Create a diagonal matrix with ones above the kth diagonal
    diagonal_matrix = np.eye(matrix.shape[0], k=k)

    # Zero out the elements below the kth diagonal
    matrix -= np.dot(diagonal_matrix, matrix)

    return matrix
