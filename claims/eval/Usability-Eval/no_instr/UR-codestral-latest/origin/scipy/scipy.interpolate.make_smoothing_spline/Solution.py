import numpy as np
from scipy.interpolate import UnivariateSpline

def compute_smoothing_spline(x, y, lam=None):
    spline = UnivariateSpline(x, y, s=lam)
    return spline.get_coeffs()

# Test the function
x = np.linspace(0, 10, 9)
y = np.sin(x)

# With lam
coeffs = compute_smoothing_spline(x, y, lam=1)
print("Coefficients with lam:", coeffs)

# Without lam (GCV criteria)
coeffs = compute_smoothing_spline(x, y)
print("Coefficients without lam:", coeffs)
