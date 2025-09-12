import scipy.stats as stats

def inverse_cdf_hermite_spline(distribution, x, order=3):
    """
    Approximates the inverse of a continuous statistical distribution's CDF
    with a Hermite spline.
    
    Parameters:
    distribution (scipy.stats.rv_continuous): Continuous statistical distribution
    x (array_like): CDF values to approximate the inverse for
    order (int, optional): Order of the Hermite spline. Default is 3.
    
    Returns:
    array_like: Inverse CDF values approximated with a Hermite spline
    """
    cdf_func = distribution.cdf
    pdf_func = distribution.pdf
    
    hermite_spline = scipy.interpolate.HermiteSpline(cdf_func(distribution.ppf(x)),
                                                    pdf_func(distribution.ppf(x)),
                                                    order=order)
    
    return distribution.ppf(hermite_spline(x))
