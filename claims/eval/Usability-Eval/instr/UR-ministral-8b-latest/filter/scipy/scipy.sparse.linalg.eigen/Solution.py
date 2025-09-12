import numpy as np
from scipy.linalg import eig

# Define your matrix A
A = np.array([[3, 2], [1, 5]])

# Calculate eigenvalues and eigenvectors
eigenvalues, eigenvectors = eig(A)

# Select the top k eigenvalues and eigenvectors
k = 1  # Replace with desired value of k
select_index = np.argsort(-np.abs(eigenvalues[:]))[:k]
selected_eigenvalues = eigenvalues[select_index]
selected_eigenvectors = eigenvectors[:, select_index]

# Output the results
print(f"Selected eigenvalues: {selected_eigenvalues}")
print(f"Selected eigenvectors:\n{selected_eigenvectors}")
