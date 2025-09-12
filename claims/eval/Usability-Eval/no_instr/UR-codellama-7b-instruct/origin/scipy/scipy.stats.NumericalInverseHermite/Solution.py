
import numpy as np
from scipy.interpolate import hermitespline

# Define a function that takes a value from the distribution and returns its corresponding quantile
def approx_inverse(value, dist):
    # Create a new scipy.stats object for the desired distribution
    stat = getattr(scipy.stats, dist)
    # Generate a set of samples from the distribution using the uniform distribution as a random generator
    samples = np.linspace(0, 1, num=100)
    x = stat.ppf(samples)
    # Compute the CDF values for these samples and find the one closest to the desired value
    y = stat.cdf(x)
    idx = np.argmin(np.abs(y - value))
    return x[idx]

# Use the function to approximate the inverse of a normal distribution's CDF with a Hermite spline
order = 3
x_hermite = np.linspace(0, 1, num=100)
y_hermite = hermitespline(x_hermite, order=order, dist='norm')
approx_x = approx_inverse(y_hermite, 'norm')

print('Approximate quantile of normal distribution at y = 0.5:', approx_x)
