import scipy.linalg

def pseudo_inverse_hermitian(matrix):
    return scipy.linalg.pinvh(matrix)
