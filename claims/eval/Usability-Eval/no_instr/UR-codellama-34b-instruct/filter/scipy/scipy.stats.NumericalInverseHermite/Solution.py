import numpy as np
from scipy.interpolate import hermite_splrep, hermite_splev
from scipy.stats import norm

# Define the distribution and its CDF
dist = norm(loc=0, scale=1)
cdf = dist.cdf

# Define the range of values to evaluate the CDF on
x_min, x_max = -1, 1
n_points = 50
x_values = np.linspace(x_min, x_max, n_points)

# Evaluate the CDF at each point
cdf_values = cdf(x_values)

# Define the order of the Hermite spline
order = 3

# Create a Hermite spline object
spline = hermite_splrep(x_values, cdf_values, k=order)

# Evaluate the spline at a new set of points
new_x_values = np.linspace(-1, 1, 100)
new_cdf_values = hermite_splev(new_x_values, spline)

# Plot the results
import matplotlib.pyplot as plt
plt.figure()
plt.plot(x_values, cdf_values, label='Original CDF')
plt.plot(new_x_values, new_cdf_values, label='Approximated CDF')
plt.legend()
plt.show()
