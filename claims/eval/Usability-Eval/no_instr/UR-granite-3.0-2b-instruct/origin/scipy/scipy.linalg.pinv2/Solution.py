from scipy.linalg import pinv

def compute_pseudo_inverse(matrix):
    return pinv(matrix)
