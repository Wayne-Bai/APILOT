import scipy.sparse as sp

def is_sparse_matrix_type(x):
    """
    Checks if the input is of a scipy sparse matrix type.

    Args:
        x (scipy.sparse.base.SPMATRIX or numpy array): Input to be checked.

    Returns:
        bool: True if the input is a scipy sparse matrix, False otherwise.
    """
    return isinstance(x, sp.spmatrix)

# Example usage:
matrix = sp.csc_matrix([[1, 0], [0, 2]])
print(is_sparse_matrix_type(matrix))  # Output: True

array = sp.csc_array([[1, 0], [0, 2]])
print(is_sparse_matrix_type(array))   # Output: False
