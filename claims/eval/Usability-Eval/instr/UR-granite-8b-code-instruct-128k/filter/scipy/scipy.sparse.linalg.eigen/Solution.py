import scipy
def find_keigenvalues_and_eigenvectors(A, k):
    eigenvalues, eigenvectors = scipy.linalg.eigh(A)
    return eigenvalues[:k], eigenvectors[:, :k]