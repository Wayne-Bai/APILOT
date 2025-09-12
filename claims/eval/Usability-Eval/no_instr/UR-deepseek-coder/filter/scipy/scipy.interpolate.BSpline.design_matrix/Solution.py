import scipy.sparse as sp
import numpy as np

def generate_design_matrix(data, rows, cols):
    """
    Generates a design matrix in CSR format sparse array.
    
    Parameters:
    data (list or array-like): The non-zero values to be placed in the matrix.
    rows (list or array-like): The row indices for the non-zero values.
    cols (list or array-like): The column indices for the non-zero values.
    
    Returns:
    scipy.sparse.csr_matrix: The design matrix in CSR format.
    """
    return sp.csr_matrix((data, (rows, cols)))

# Example usage:
data = [1, 2, 3, 4]
rows = [0, 1, 2, 3]
cols = [0, 1, 2, 3]
design_matrix = generate_design_matrix(data, rows, cols)
print(design_matrix)
