
import numpy as np

def einstein_sum(a, b):
    return np.einsum("ij,j->i", a, b)
