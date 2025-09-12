import scipy.sparse as sp
import numpy as np

def create_design_matrix(data, num_columns):
    """
    Create a CSR format sparse design matrix from given data.

    Parameters:
    - data (list of tuples): Each tuple represents (row_index, col_index, value)
    - num_columns (int): The number of columns in the matrix

    Returns:
    - scipy.sparse.csr_matrix: The design matrix in CSR format
    """
    # Unpack rows, columns, and values from the data tuples
    rows, cols, values = zip(*data)

    # Create a CSR matrix
    design_matrix = sp.csr_matrix((values, (rows, cols)), shape=(max(rows)+1, num_columns))

    return design_matrix

# Example usage:
data = [(0, 0, 1), (0, 1, 2), (1, 0, 3), (1, 1, 4), (2, 0, 5)]
num_columns = 2
matrix = create_design_matrix(data, num_columns)
print(matrix.toarray())
