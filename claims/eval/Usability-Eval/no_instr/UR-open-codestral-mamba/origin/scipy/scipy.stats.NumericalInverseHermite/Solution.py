import scipy.special as scs

def inverse_cdf_hermite(x, order=3):
    """
    create a Hermite spline approximation of the inverse CDF
    x : array_like
        Input array containing (0 to 1) values for the inverse CDF
    order : int, optional
        Order of the Hermite spline, by default 3
    return : array_like
        Value of the inverse CDF at points corresponding to x.
    """
    if (x < 0).any() or (x > 1).any():
        raise ValueError("`x` must only contain values in [0, 1]")

    # Compute the polynomial coefficients of the Hermite spline approximation of the CDF
    h = scs.hermite(order)
    cdf_coeffs = scs.norm.cdf(scs.norm.ppf((x / 100).tolist(), loc=0, scale=1))
    cdf_poly_coeffs = h(scs.norm.ppf(cdf_coeffs))

    # Use numpy's polyfit to find the coefficients of the best fitting polynomial through the CDF
    # then use numpy's roots to find points where the polynomial is zero (the inverse CDF)
    poly_coeffs = scs.polyfit(cdf_coeffs, cdf_poly_coeffs, order)
    return scs.roots(poly_coeffs[::-1])  # Reverse order of coefficients because polyfit uses reversed order of inputs

# Test the function
print(inverse_cdf_hermite([1, 10, 50, 90, 99, 100])) # This should give [0., 0.1, 1.28, 1.64, 2.33, 2.807]
