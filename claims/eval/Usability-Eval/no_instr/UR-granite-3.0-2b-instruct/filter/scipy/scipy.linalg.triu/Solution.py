import numpy as np
from scipy.linalg import circulant

def zero_below_kth_diagonal(matrix, k):
    n = len(matrix)
    k = min(k, n)

    # Create a circulant matrix with the same shape as the input matrix
    circulant_matrix = circulant(matrix[0])

    # Calculate the circulant matrix raised to the power of k
    circulant_matrix_k = np.linalg.matrix_power(circulant_matrix, k)

    # Multiply the circulant matrix raised to the power of k with the input matrix
    result = circulant_matrix_k @ matrix

    return result
