from scipy import interpolate
import numpy as np

def compute_smoothing_spline(x, y, lam=None):
    if lam is None:
        lam = interpolate.splrep(x, y, s=0)[1]
    tck = interpolate.splrep(x, y, task=0, s=lam)
    return tck

# Example usage
x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([0, 1, 0, 1, 0, 1])
print(compute_smoothing_spline(x, y))
