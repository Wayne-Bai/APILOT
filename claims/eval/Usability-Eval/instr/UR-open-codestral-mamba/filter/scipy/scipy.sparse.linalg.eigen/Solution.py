import numpy as np
from scipy.linalg import eigh

# Assume a simple square matrix
A = np.array([[1, 2], [3, 4]])

# Use eigh function to find eigenvalues and eigenvectors
eigenValues, eigenVectors = eigh(A)

# Print the eigenvalues and eigenvectors
print('Eigenvalues:', eigenValues)
print('Eigenvectors:', eigenVectors)
