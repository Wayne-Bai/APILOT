import numpy as np

# Let's assume we have a 3x3 square array
array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# We can compute the eigenvalues and right eigenvectors as follows:
eigenvalues, eigenvectors = np.linalg.eig(array)

print("Eigenvalues:")
print(eigenvalues)
print("\nRight eigenvectors:")
print(eigenvectors)
