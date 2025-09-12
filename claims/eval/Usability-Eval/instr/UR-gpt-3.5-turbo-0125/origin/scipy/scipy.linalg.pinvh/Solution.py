
import numpy as np
from scipy.linalg import svd

def hermitian_pinv(matrix):
    U, s, Vh = svd(matrix)
    s_pseudo_inv = np.zeros((matrix.shape[1], matrix.shape[0]))
    s_pseudo_inv[:len(s), :len(s)] = np.diag(1/s)
    pseudo_inv = np.dot(Vh.T, np.dot(s_pseudo_inv, U.T))
    return pseudo_inv

# Example usage
matrix = np.array([[1, -1j], [1j, 2]])
pseudo_inv = hermitian_pinv(matrix)
print("Pseudo-inverse of the matrix:")
print(pseudo_inv)
