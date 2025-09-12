
import numpy as np

def pseudo_inverse(matrix):
    U, s, VT = np.linalg.svd(matrix)
    s_plus = np.zeros((VT.shape[0], U.shape[1]))
    s_plus[:len(s)] = np.where(s > 0, 1/s, 0)
    pseudo_inverse = VT.T @ np.diag(s_plus) @ U.T
    return pseudo_inverse

# Example usage
matrix = np.array([[1, 2], [3, 4], [5, 6]])
pseudo_inv = pseudo_inverse(matrix)
print("Pseudo Inverse:")
print(pseudo_inv)
