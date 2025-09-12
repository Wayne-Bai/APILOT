# Import the numpy library
import numpy as np

# Create a real symmetric matrix
A = np.array([[1, 2, 3], [2, 4, 5], [3, 5, 6]])

# Create a complex Hermitian (conjugate symmetric) matrix
B = np.array([[1 + 2j, 3 - 4j, 5 + 6j], 
              [3 + 4j, 2 - 1j, 7 - 8j], 
              [5 - 6j, 7 + 8j, 9 + 0j]])

# Calculate the eigenvalues and eigenvectors of A
eigenvalues_A, eigenvectors_A = np.linalg.eigh(A)

# Calculate the eigenvalues and eigenvectors of B
eigenvalues_B, eigenvectors_B = np.linalg.eigh(B)

# Print the results for A
print("Eigenvalues of A:")
print(eigenvalues_A)
print("Eigenvectors of A:")
print(eigenvectors_A)

# Print the results for B
print("Eigenvalues of B:")
print(eigenvalues_B)
print("Eigenvectors of B:")
print(eigenvectors_B)
