import scipy as sp
import numpy as np

def generate_design_matrix(n_samples, n_features):
    """
    Returns a design matrix as a CSR format sparse array.
    
    Parameters:
    n_samples (int): Number of samples in the design matrix.
    n_features (int): Number of features in the design matrix.
    
    Returns:
    scipy.sparse.csr_matrix: A CSR format sparse array representing the design matrix.
    """
    
    # Create a random dense matrix
    dense_matrix = np.random.rand(n_samples, n_features)
    
    # Convert the dense matrix to a CSR format sparse array
    csr_matrix = sp.sparse.csr_matrix(dense_matrix)
    
    return csr_matrix

# Example usage:
n_samples = 100
n_features = 50
design_matrix = generate_design_matrix(n_samples, n_features)
print(design_matrix)
