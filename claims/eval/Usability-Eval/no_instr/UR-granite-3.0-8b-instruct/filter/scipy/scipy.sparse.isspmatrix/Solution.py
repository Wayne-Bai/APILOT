import scipy.sparse

def is_sparse_matrix(x):
    return isinstance(x, scipy.sparse.spmatrix)
