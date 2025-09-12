from scipy.interpolate import make_interp_spline

def quadratic_bspline(x, y):
    """
    Generate a quadratic B-spline from the given data points (x, y).

    Parameters:
    x (array_like): x-coordinates of the data points.
    y (array_like): y-coordinates of the data points.

    Returns:
    spline (scipy.interpolate.BSpline): The quadratic B-spline.
    """
    # Create a cubic B-spline from the data points
    spline = make_interp_spline(x, y, k=3)

    # Set the degree of the spline to 2 to obtain a quadratic B-spline
    spline.set_derivative(2)

    return spline
