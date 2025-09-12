import numpy as np

# Example square array (2x2 in this case)
array = np.array([[4, 1], [2, 3]])

# Compute eigenvalues using np.linalg.eig
eigenvalues, eigenvectors = np.linalg.eig(array)

# Display the results
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:")
for vector in eigenvectors:
    print(vector)
