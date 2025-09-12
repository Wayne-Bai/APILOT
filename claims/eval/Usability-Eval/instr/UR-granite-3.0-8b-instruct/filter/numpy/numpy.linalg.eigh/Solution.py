import numpy as np

def eigen(A):
    # Check if the matrix is Hermitian or symmetric
    if np.allclose(A, A.conj().T) or np.allclose(A, A.T):
        # Compute the eigenvalues and eigenvectors
        eigenvalues, eigenvectors = np.linalg.eig(A)
        return eigenvalues, eigenvectors
    else:
        raise ValueError("Matrix must be Hermitian or symmetric")
