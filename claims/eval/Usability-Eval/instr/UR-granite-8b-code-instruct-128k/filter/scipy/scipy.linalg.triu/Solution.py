import numpy as np

def zero_elements_below_kth_diagonal(matrix, k):
    if k < 0:
        raise ValueError("k must be a non-negative integer")
    
    m, n = matrix.shape
    if k >= m or k >= n:
        raise ValueError("k is out of bounds for the given matrix")
    
    zeroed_matrix = matrix.copy()
    for i in range(m):
        for j in range(n):
            if i > j + k:
                zeroed_matrix[i, j] = 0
    
    return zeroed_matrix