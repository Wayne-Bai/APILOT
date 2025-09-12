
import numpy as np
from scipy.interpolate import CubicSpline

# Define data points for which we want to find the smoothing cubic spline function
x = np.linspace(0, 10, 50)
y = np.sin(x) + np.random.randn(len(x)) * 0.1

# Define lam value or use GCV criteria to find it if not specified
lam = None
if lam is None:
    # Use GCV (Generalized Cross Validation) to find the optimal lam value
    from scipy.interpolate import SmoothBivariateSpline
    spline = SmoothBivariateSpline(x, y)
    lam, _, _, _ = spline.gcv()

# Compute the coefficients of the smoothing cubic spline function using lam
spline = CubicSpline(x, y, lambda_=lam)
coeffs = spline.c
