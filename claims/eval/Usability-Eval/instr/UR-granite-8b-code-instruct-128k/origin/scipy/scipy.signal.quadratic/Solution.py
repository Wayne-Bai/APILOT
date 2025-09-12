from scipy.interpolate import bspline
def quadratic_bspline(x):
    return bspline(x, 2)
