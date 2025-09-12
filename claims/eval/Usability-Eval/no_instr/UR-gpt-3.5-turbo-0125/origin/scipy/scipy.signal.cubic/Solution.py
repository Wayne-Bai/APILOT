
from scipy.interpolate import bspline

def cubic_b_spline(x):
    return bspline(x, 3)
