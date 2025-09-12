
from scipy import interpolate

def cubic_bspline(x):
    return interpolate.splrep(x, x, k=3)
