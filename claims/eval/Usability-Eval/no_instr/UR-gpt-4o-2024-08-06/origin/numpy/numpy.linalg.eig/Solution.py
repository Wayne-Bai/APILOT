import numpy as np

# Define the square matrix
A = np.array([[1, 2], [3, 4]])

# Compute the eigenvalues and right eigenvectors
eigenvalues, right_eigenvectors = np.linalg.eig(A)

# Display the results
print("Eigenvalues:", eigenvalues)
print("Right eigenvectors:\n", right_eigenvectors)
