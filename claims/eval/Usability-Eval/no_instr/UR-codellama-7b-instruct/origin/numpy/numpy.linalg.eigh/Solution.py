import numpy as np

def get_eigenvalues_and_vectors(matrix):
    # Check if the input is a real or complex matrix
    is_real = np.allclose(np.imag(matrix), 0)

    # Calculate the eigenvalues and eigenvectors using numpy's built-in functions
    if is_real:
        w, v = np.linalg.eigh(matrix)
    else:
        w, v = np.linalg.eig(matrix)

    # Return the eigenvalues and eigenvectors as a tuple of arrays
    return (w, v)
