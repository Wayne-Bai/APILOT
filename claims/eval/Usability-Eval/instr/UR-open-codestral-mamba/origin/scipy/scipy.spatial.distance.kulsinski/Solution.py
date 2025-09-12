from scipy.spatial.distance import pdist, squareform
from scipy.stats import ks_2samp
import numpy as np

def kulsinski(a, b):
    # a and b are boolean 1-D arrays

    a = np.asarray(a).astype(np.int)
    b = np.asarray(b).astype(np.int)

    if a.shape != b.shape:
        raise ValueError('Input arrays must have the same shape.')

    n1, n2, e11, e12, e21, e22 = 0, 0, 0, 0, 0, 0

    for i in range(a.size):
        if a[i] == 1 and b[i] == 1:
            n1 += 1
        elif a[i] == 1 and b[i] == 0:
            e12 += 1
        elif a[i] == 0 and b[i] == 1:
            e21 += 1
        elif a[i] == 0 and b[i] == 0:
            n2 += 1
        else:
            raise ValueError('Invalid input arrays.')

    e11 = n1 - e12
    e22 = n2 - e21

    ks = 1 - (2 * (n1 * n2 - e12 * e21)) / ((n1 + e12) * (n2 + e21))

    return ks

a = [True, False, True, True, False, True, False, False, True, True]
b = [True, True, False, True, True, False, True, False, False, False]

print(kulsinski(a, b))
