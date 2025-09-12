import numpy as np
from scipy import linalg

# Define a Hermitian matrix (a square matrix that is equal to its own conjugate transpose)
# Here we generate a 2x2 matrix, but you can replace it with any Hermitian matrix
A = np.array([[1, 1+1j], [1-1j, 1]])

# Compute the conjugate transpose of A (np.conj(A).T)
A_conj_T = np.conj(A).T

# Check if A is Hermitian
print("Is A Hermitian?", np.allclose(A, A_conj_T))

# Compute the Moore-Penrose pseudo-inverse of A using the pinv function from scipy.linalg
A_pinv = linalg.pinv(A)

# Print the pseudo-inverse of A
print("Pseudo-inverse of A:")
print(A_pinv)
