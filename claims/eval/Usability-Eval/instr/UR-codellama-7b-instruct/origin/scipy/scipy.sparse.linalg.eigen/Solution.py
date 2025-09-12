
import numpy as np
from scipy import linalg

# Define the square matrix A
A = np.array([[1, 2], [3, 4]])

# Find the eigenvalues and eigenvectors of A
eigen_vals, eigen_vecs = linalg.eig(A)
