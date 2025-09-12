
import numpy as np

# Create a square array (replace with your array)
A = np.array([[1, 2], [3, 4]])

# Compute the eigenvalues and right eigenvectors
eigenvalues, right_eigenvectors = np.linalg.eig(A)

print("Eigenvalues:")
print(eigenvalues)
print("\nRight Eigenvectors:")
print(right_eigenvectors)
