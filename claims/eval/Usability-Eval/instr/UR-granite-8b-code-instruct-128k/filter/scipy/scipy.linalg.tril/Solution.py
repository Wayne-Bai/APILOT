
import numpy as np
def zero_matrix_above_kth_diagonal(matrix, k):
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if i > j and k > j:
                matrix[i, j] = 0
            elif i < j and k < i:
                matrix[i, j] = 0
    return matrix
