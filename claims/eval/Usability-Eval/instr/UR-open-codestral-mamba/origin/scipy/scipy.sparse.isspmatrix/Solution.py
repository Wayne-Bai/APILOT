import scipy
from scipy.sparse import isspmatrix

def is_sparse(x):
    return isspmatrix(x)
