
import numpy as np

# Create a square array
array = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

# Compute the eigenvalues and right eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(array)

print("Eigenvalues:")
print(eigenvalues)

print("\nRight Eigenvectors:")
print(eigenvectors)
