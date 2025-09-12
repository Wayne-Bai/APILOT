from scipy.linalg import pinv

# Assuming 'A' is your matrix
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Compute the Moore-Penrose pseudo-inverse of A
A_pinv = pinv(A)

print(A_pinv)
