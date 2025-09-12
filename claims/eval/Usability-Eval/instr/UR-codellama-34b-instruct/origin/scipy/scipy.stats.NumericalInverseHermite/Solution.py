import numpy as np
from scipy.interpolate import interp1d

# Define the CDF and its inverse
def cdf(x):
    return 0.5 * (1 + erf(x / sqrt(2)))

def inv_cdf(y):
    return sqrt(2) * erfinv(2 * y - 1)

# Define the Hermite spline approximation
order = 3 # degree of the Hermite spline
nodes = np.linspace(-5, 5, num=100) # nodes for the spline
cdfs = cdf(nodes)
interp_fun = interp1d(cdfs, nodes, kind='cubic')

# Evaluate the Hermite spline at a point
x = -2.5
y = inv_cdf(x)
print(f"The approximate inverse of {x} is {y}")
