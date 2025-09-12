
import numpy as np

# Define the array for which we want to compute the eigenvalues and right eigenvectors
array = np.array([[1, 2], [3, 4]])

# Compute the eigenvalues and right eigenvectors using NumPy's eig function
eigenvalues, eigenvectors = np.linalg.eig(array)

# Print the results
print("Eigenvalues:")
print(eigenvalues)
print("\nRight Eigenvectors:")
print(eigenvectors)
