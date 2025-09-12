import scipy.sparse as sps
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
    # Ensure data, rows, and cols are numpy arrays
    data = np.array(data)
    rows = np.array(rows)
    cols = np.array(cols)

    # Create the CSR matrix
    design_matrix = sps.csr_matrix((data, (rows, cols)))

    return design_matrix

# Example usage:
data = [1, 2, 3, 4]
rows = [0, 1, 2, 3]
cols = [0, 1, 2, 3]

design_matrix = generate_design_matrix(data, rows, cols)
print(design_matrix)
