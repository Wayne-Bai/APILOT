
import numpy as np

# Define a complex Hermitian matrix
M = np.array([[1+2j, 3-4j], [3-4j, 5+6j]])

# Compute the eigenvalues and eigenvectors using numpy's linalg.eig() function
evals, evecs = np.linalg.eig(M)

print("Eigenvalues:", evals)
print("Eigenvectors:", evecs)
