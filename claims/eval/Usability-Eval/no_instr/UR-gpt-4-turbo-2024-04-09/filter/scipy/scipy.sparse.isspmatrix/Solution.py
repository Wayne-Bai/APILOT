import scipy.sparse

def is_sparse_matrix(x):
    return scipy.sparse.issparse(x)

# Example usage
if __name__ == "__main__":
    # Sample data for demonstration
    from scipy.sparse import csr_matrix
    x = csr_matrix([[1, 0], [0, 2]])
    
    print(is_sparse_matrix(x))  # Output: True
    
    y = [[1, 0], [0, 2]]  # This is a regular list, not a sparse matrix
    print(is_sparse_matrix(y))  # Output: False
