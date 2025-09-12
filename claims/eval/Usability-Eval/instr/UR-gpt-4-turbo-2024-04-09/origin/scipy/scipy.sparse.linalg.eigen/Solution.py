import scipy.linalg as la

def find_eigenvalues_eigenvectors(A, k):
    # Compute the eigenvalues and eigenvectors using scipy.linalg.eig
    eigenvalues, eigenvectors = la.eig(A)
    
    # Since la.eig returns complex numbers, they are sorted based on the magnitude of eigenvalues
    idx = eigenvalues.argsort()[::-1]
    eigenvalues = eigenvalues[idx]
    eigenvectors = eigenvectors[:,idx]
    
    # Select the first k eigenvalues and corresponding eigenvectors
    selected_eigenvalues = eigenvalues[:k]
    selected_eigenvectors = eigenvectors[:, :k]
    
    return selected_eigenvalues, selected_eigenvectors
