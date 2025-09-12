
import numpy as np
from scipy.linalg import eigs

# Generate a random square matrix A with dimensions n x n
n = 10
A = np.random.rand(n, n)

# Find k eigenvalues and eigenvectors of A
k = 3
eigenvalues, eigenvectors = eigs(A, k=k, which='LM')

print('Eigenvalues:', eigenvalues)
print('Eigenvectors:\n', eigenvectors)
