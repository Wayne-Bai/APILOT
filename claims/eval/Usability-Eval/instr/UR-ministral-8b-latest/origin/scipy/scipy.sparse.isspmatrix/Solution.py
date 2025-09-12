import scipy.sparse

def is_sparse_matrix(x):
    return isinstance(x, scipy.sparse._sparsetools_matrix.RefValidMatrix)

# Example usage
if __name__ == "__main__":
    import numpy as np
    from scipy.sparse import csr_matrix

    # Create a sparse matrix
    sparse_matrix = csr_matrix(np.array([[1, 2], [3, 4]]))

    # Check if x is a sparse matrix
    print(is_sparse_matrix(sparse_matrix))  # Should print: True

    # Create a dense matrix
    dense_matrix = np.array([[1, 2], [3, 4]])

    # Check if x is a sparse matrix
    print(is_sparse_matrix(dense_matrix))  # Should print: False
