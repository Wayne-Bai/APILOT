import numpy as np
from scipy.interpolate import BSPline

def cubic_b_spline_interpolation(x, y):
    # Create B-spline objects for cubic B-splines
    cubic_bspline = BSPline(k=3, x=x, y=y)

    return cubic_bspline

# Example usage
x = np.array([0, 2, 3, 5, 7, 9])
y = np.array([1, 3, 4, 3, 2, 1])
cubic_bspline = cubic_b_spline_interpolation(x, y)

cubic_bspline

