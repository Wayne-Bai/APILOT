import numpy as np

# Define a square array
A = np.array([[4, 2],
              [1, 3]])

# Calculate the eigenvalues and right eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalues:", eigenvalues)
print("Right eigenvectors:", eigenvectors)
