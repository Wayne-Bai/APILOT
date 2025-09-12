import numpy as np
from scipy import logical_and, logical_or, logical_not

def kulsinski_dissimilarity(a, b):
    fp = np.sum(logical_and(logical_not(a), b))
    fn = np.sum(logical_and(a, logical_not(b)))
    return (fp + fn) / len(a)
