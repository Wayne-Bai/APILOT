import numpy as np

# Define a sample square array
arr = np.array([[1, 2], [3, 4]])

# Compute the eigenvalues and right eigenvectors of the array
eigenvalues, right_eigenvectors = np.linalg.eig(arr)

# Print the eigenvalues and right eigenvectors
print("Eigenvalues:")
print(eigenvalues)
print("Right Eigenvectors:")
print(right_eigenvectors)
