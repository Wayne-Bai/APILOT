
import scipy
def is_sparse(x):
    """
    Check if x is a sparse matrix
    """
    return scipy.sparse.issparse(x)
