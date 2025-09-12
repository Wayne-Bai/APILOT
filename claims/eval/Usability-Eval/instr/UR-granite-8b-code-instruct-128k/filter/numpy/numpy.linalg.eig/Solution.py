import numpy as np

# Create a square array
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Compute the eigenvalues and right eigenvectors
eigenvalues, right_eigenvectors = np.linalg.eig(A)

# Print the results
print("Eigenvalues:")
print(eigenvalues)
print("Right Eigenvectors:")
print(right_eigenvectors)
