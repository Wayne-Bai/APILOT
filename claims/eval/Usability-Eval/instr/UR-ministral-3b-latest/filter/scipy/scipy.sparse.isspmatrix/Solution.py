import scipy.sparse

def is_sparse_matrix(x):
    return isinstance(x, scipy.sparse.spmatrix)

# Example usage:
arr = [[1, 2], [3, 4]]
sparse_matrix = scipy.sparse.csr_matrix(arr)

print(is_sparse_matrix(arr))  # Should return False
print(is_sparse_matrix(sparse_matrix))  # Should return True
