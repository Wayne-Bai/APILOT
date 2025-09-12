
import numpy as np
from scipy.interpolate import CubicSpline

def smoothing_cubic_spline(x, y, lam=None):
    if lam is not None:
        spline = CubicSpline(x, y, bc_type='clamped', extrapolate=True, axis=0).smooth(lam)
    else:
        spline = CubicSpline(x, y, bc_type='clamped', extrapolate=True, axis=0).smooth('gcv')
        
    return spline.c

# Example usage:
x = np.array([1, 2, 3, 4, 5])
y = np.array([4, 2, 5, 1, 3])

coefficients = smoothing_cubic_spline(x, y, lam=0.1)
print(coefficients)
