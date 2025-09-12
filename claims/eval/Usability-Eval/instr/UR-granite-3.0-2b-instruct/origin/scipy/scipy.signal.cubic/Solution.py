from scipy.interpolate import make_bspline

def cubic_bspline(x):
    bspline = make_bspline(x, k=3)
    return bspline(x)
