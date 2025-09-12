
import numpy as np
from scipy.sparse import spmatrix

def is_sparse_matrix(x):
    return isinstance(x, spmatrix)
