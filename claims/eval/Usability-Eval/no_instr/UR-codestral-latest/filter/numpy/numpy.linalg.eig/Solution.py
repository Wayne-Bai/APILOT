import numpy as np

# Let's define a square array
A = np.array([[1, 2], [3, 4]])

# Compute the eigenvalues and right eigenvectors using np.linalg.eig
eigenvalues, right_eigenvectors = np.linalg.eig(A)

print("Eigenvalues:")
print(eigenvalues)

print("\nRight Eigenvectors:")
print(right_eigenvectors)
