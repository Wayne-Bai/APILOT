from scipy.interpolate import make_spline

def cubic_bspline(x, y):
    # Create a cubic B-spline spline from the data points
    spline = make_spline(x, y, k=3)

    # Return the spline
    return spline
