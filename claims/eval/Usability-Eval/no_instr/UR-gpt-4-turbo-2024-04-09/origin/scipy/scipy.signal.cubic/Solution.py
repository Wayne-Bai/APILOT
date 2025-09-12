import scipy.interpolate as interpolate

def cubic_bspline(x):
    return interpolate.bspline(x, 3)
