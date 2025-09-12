import scipy.linalg

def compute_pseudo_inverse(matrix):
    return scipy.linalg.pinv(matrix)
