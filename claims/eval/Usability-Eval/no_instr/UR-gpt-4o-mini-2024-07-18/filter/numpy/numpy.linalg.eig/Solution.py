import numpy as np

# Define the square array (matrix)
A = np.array([[4, -2],
              [1, 1]])

# Compute the eigenvalues and right eigenvectors
eigenvalues, right_eigenvectors = np.linalg.eig(A)

# Output the results
print("Eigenvalues:")
print(eigenvalues)
print("Right Eigenvectors:")
print(right_eigenvectors)
