import scipy.interpolate as interpolate
import numpy as np

# Assuming x and y as input data sets
x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([0, 1, 4, 9, 16, 25])

# Computing smoothing cubic spline
lam = 0.5  # Set lam to control the trade-off between smoothness and goodness of fit
if lam is None:
    # Compute the smoothing factor using generalized cross-validation
    lam, c, k, _ = interpolate.splrep(x, y, s=0)

# Computing the smoothing cubic spline
smoothing_spline = interpolate.BSpline(c, k)

# Output the computed smoothing cubic spline
print(smoothing_spline)
