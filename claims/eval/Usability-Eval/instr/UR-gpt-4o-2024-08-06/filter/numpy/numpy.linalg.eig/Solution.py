import numpy as np

# Define the input square array
A = np.array([[4, -2], 
              [1, 1]])

# Compute the eigenvalues and right eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalues:", eigenvalues)
print("Right Eigenvectors:\n", eigenvectors)
