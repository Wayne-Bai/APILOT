import numpy as np
import scipy.special as sp
import scipy.spline as spl

def BsplineBasis(c, d, i, k, n):
    """
    Generate the B-spline basis function of order k.
    """
    n_p + 1
    if k == 0:
        return c[i]
    elif i + 1 == len(c) and d[i] == 0:
        return 1
    elif i + 1 == len(c):
        return 0
    elif d[i] == 0:
        return 0

    Bin = BsplineBasis(c + d, d, i + 1, k - 1, n) / (c[i + k] - c[i + 1])
    Bkmin1 = BsplineBasis(c + d, d, i, k - 1, n) / (c[i + k] - c[i])

    return Bin + (c[i + k] - c[i]) * Bkmin1

# Example Usage:
c = np.array([0, 0, 5, 5])
d = np.array([1, 2, 1, 0])
n = 3
order = 2
for i in range(n + 1):
    basis_func = BsplineBasis(c, d, i, order, n)
    print(f"B-spline basis function at node {i}: {basis_func}")
