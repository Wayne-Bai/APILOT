import scipy.sparse as sparse
import numpy as np

# Function to check if matrix is sparse
def is_sparse(matrix):
    try:
        # Check if matrix is scipy sparse
        if isinstance(matrix, (sparse.coo_matrix, sparse.csc_matrix, sparse.csr_matrix, sparse.bsr_matrix, sparse.dia_matrix, sparse.dok_matrix, sparse.lil_matrix)):
            return True
    except TypeError:
        # If not scipy sparse, check if matrix is numpy and has more than 90% zeros
        if isinstance(matrix, np.ndarray):
            if matrix.size > 0 and np.count_nonzero(matrix) / matrix.size < 0.1:
                return True
    return False

# Testing the function
# Create a scipy csr_matrix
scipy_sparse_matrix = sparse.csr_matrix(np.array([[0, 2, 0], [0, 0, 3], [4, 0, 0]]))
print(is_sparse(scipy_sparse_matrix))  # Should return True

# Create a numpy array
numpy_sparse_array = np.array([[0, 2, 0], [0, 0, 3], [4, 0, 0]])
print(is_sparse(numpy_sparse_array))  # Should return True

# Create a numpy dense array
numpy_dense_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(is_sparse(numpy_dense_array))  # Should return False
