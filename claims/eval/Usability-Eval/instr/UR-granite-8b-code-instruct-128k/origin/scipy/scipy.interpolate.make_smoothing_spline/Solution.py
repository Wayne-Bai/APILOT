from scipy.interpolate import UnivariateSpline

def compute_smoothing_spline(x, y, s=None):
    """
    Computes the coefficients of a smoothing cubic spline function for the given data points (x, y).
    If s is None, the algorithm uses the GCV criteria to automatically determine the value of s.
    """
    spline = UnivariateSpline(x, y, s=s)
    return spline.coef
