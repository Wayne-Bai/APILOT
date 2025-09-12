from scipy.linalg import eig

# Assuming A is your square matrix
A = [[1, 2], [3, 4]]  # replace this with your matrix

# Find k eigenvalues and eigenvectors
k = 2
eigenvalues, eigenvectors = eig(A, k)

print("Eigenvalues: ", eigenvalues)
print("Eigenvectors: ", eigenvectors)
