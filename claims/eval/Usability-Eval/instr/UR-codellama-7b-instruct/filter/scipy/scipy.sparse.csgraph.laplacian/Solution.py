import numpy as np
from scipy.sparse import diags, dia_matrix

def laplacian(A):
    n = A.shape[0]
    D = diags(A.sum(1))
    L = D - A
    return L
