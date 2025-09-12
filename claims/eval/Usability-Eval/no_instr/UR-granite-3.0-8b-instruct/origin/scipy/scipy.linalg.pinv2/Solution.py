from scipy.linalg import pinv

# Assuming 'matrix' is the input matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Compute the Moore-Penrose pseudo-inverse
pseudo_inverse = pinv(matrix)

print(pseudo_inverse)
