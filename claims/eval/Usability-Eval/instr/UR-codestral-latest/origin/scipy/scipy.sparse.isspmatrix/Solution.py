import scipy.sparse

def is_sparse(x):
    return isinstance(x, scipy.sparse.spmatrix)

# For example:
from scipy.sparse import csr_matrix
sparse_matrix = csr_matrix([[1,0,0],[0,0,3],[0,0,0]])
print(is_sparse(sparse_matrix))  # Should print True
