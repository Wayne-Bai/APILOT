import scipy.interpolate as interpolate
import numpy as np

def inverse_hermite_spline(distribution, x, order):
    # Generate a set of sample points and evaluate the CDF at those points
    samples = np.linspace(0, 1, 1000)
    cdf_values = distribution.cdf(samples)
    
    # Fit a Hermite spline to the CDF values
    spline = interpolate.HermiteSpline(samples, cdf_values, order)
    
    # Evaluate the inverse of the spline at the given x values
    inverse_values = spline.inverse(x)
    
    return inverse_values
