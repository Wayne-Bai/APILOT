import numpy as np

# assuming we have a 3x3 square array
array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# compute eigenvalues and eigenvectors
eigvals, eigvects = np.linalg.eig(array)

eigvals, eigvects
