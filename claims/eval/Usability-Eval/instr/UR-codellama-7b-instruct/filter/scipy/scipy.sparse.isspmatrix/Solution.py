
import scipy.sparse as sp

def is_sparse(x):
    return sp.isspmatrix(x)
