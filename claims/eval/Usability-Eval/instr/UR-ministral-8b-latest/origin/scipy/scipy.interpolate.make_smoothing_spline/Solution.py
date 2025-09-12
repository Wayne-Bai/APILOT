import scipy.interpolate
import numpy as np

def cubic_spline(samples):
    """
    Compute the (coefficients of) smoothing cubic spline function.
    """
    # Compute the estimated np for GCV
    n = len(samples)
    spline = scipy.interpolate.CubicSpline(samples[:, 0], samples[:, 1])
    estimated_np_gcv = spline.cv()

    # If lambda is None, calculate it using the GCV criterion
    if lambda_ is None:
        lambda_ = 2. * estimated_np_gcv**2 / np.log(n)

    spline = scipy.interpolate.CubicSpline(samples[:, 0], samples[:, 1], bc_type='natural', lmbda=lambda_)

    smoothing_cubic_spline = spline
    return smoothing_cubic_spline
