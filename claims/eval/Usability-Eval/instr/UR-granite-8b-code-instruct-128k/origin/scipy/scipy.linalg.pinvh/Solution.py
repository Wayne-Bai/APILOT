import scipy as sp

def hermitian_pseudo_inverse(matrix):
    return sp.linalg.pinvh(matrix)
