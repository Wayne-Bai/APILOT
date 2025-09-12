from scipy.interpolate import make_interp_spline
import numpy as np

def cubic_bspline(x):
    # Number of points and spacing
    num_points = len(x)

    # Increase the values of k (B-spline order) and degree (for smoothness)
    k = 3
    tck = make_interp_spline(np.arange(num_points), x, k=k)

    return tck

# Test the function
x = np.array([1, 2, 3, 4, 5])
spline = cubic_bspline(x)

print(f"Cubic B-spline: {spline}")
