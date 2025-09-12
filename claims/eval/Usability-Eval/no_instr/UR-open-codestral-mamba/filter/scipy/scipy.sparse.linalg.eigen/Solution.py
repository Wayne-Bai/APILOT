# Import the necessary library
import scipy
from scipy.linalg import eig

# Define a square matrix A
A = [[3, 2], [1, 4]]

# Use the eig function from the linalg module in scipy
eigenvalues, eigenvectors = eig(A)

# Get the first k eigenvalues and eigenvectors
k = 2  # or any other desired number
k_eigenvalues = eigenvalues[:k]
k_eigenvectors = eigenvectors[:, :k]

# Print the k eigenvalues and eigenvectors
print(f'First {k} eigenvalues: {k_eigenvalues}')
print(f'First {k} eigenvectors:\n{k_eigenvectors}')
