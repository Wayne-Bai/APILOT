import scipy.sparse

def is_sparse_matrix(x):
    return scipy.sparse.issparse(x)
