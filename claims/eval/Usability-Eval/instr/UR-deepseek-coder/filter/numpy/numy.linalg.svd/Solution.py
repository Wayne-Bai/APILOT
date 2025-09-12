import numpy as np

def svd(matrix):
    # Perform Singular Value Decomposition
    U, S, VT = np.linalg.svd(matrix, full_matrices=False)
    return U, S, VT

# Example usage:
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
U, S, VT = svd(matrix)

print("U:\n", U)
print("S:\n", S)
print("VT:\n", VT)
