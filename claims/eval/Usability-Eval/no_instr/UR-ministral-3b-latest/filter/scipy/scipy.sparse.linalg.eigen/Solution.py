from scipy.linalg import eigh
import numpy as np

A = np.array([[4, 1, 2],
              [1, 4, 1],
              [2, 1, 3]])

eigenvalues, eigenvectors = eigh(A)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)
