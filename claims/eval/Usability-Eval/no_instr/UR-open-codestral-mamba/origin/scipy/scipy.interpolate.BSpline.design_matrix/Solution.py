from scipy import sparse
import numpy as np

def design_matrix_to_csr(X):
    """
    Convert a design matrix to a CSR format sparse array.

    Parameters:
    X (numpy array): Design matrix.

    Returns:
    csr_matrix: CSR format sparse array of the design matrix.
    """
    # Convert design matrix to CSR format
    csr_matrix = sparse.csr_matrix(X)

    return csr_matrix

# Usage example
X = np.array([[0, 1, 0], [2, 0, 3]])
csr = design_matrix_to_csr(X)
print(csr)
