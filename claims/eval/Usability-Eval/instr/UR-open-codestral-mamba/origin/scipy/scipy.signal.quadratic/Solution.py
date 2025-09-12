import scipy.interpolate as spi
import numpy as np

# Define a function to generate quadratic B-spline
def quadratic_bspline(x, k=2):
    # Define the knot points for generating the spline
    tck = knot_points(x, k)
    # Generate the B-spline
    return spi.splev(x, tck)

# Define a function to generate knot points for spline
def knot_points(x, k):
    n = len(x)
    t = [x[0]] * (k + 1) + list(x) + [x[-1]] * (k + 1)
    u = np.linspace(0, len(x) + k - 1, len(x) + k - 1)
    tck = [t, u, k]
    return tck

# Generate a set of points for the quadratic B-spline
x = np.linspace(-10, 10, 100)
y = quadratic_bspline(x)

# Plot the quadratic B-spline
plt.plot(x, y)
plt.title('Quadratic B-spline')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
