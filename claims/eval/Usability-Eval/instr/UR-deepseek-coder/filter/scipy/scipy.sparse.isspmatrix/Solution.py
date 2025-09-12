import scipy.sparse as sp

def is_sparse_matrix(x):
    return isinstance(x, sp.spmatrix)
