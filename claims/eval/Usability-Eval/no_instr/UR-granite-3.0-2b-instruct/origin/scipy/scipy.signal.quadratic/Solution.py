from scipy.interpolate import make_bspline

def quadratic_bspline(x, y):
    # Create a quadratic B-spline from the given data points
    bsp = make_bspline(x, y, k=2)

    # Evaluate the B-spline at a new set of x-coordinates
    x_new = ...  # Replace ... with the desired x-coordinates
    y_new = bsp(x_new)

    return y_new
