import scipy.sparse as sp
import numpy as np

def create_design_matrix(matrix_size, density=0.1):
    """
    Creates a design matrix in CSR format with the specified size and density.
    
    Args:
    matrix_size (tuple): the shape of the matrix (rows, columns).
    density (float): the density of the non-zero elements in the matrix.

    Returns:
    scipy.sparse.csr_matrix: CSR format sparse array representing the design matrix.
    """
    # Generate a random sparse matrix as the design matrix
    design_matrix = sp.random(matrix_size[0], matrix_size[1], density=density, format='csr')
    
    return design_matrix

# Example usage:
rows, cols = 1000, 500
design_matrix = create_design_matrix((rows, cols))
print(design_matrix)
