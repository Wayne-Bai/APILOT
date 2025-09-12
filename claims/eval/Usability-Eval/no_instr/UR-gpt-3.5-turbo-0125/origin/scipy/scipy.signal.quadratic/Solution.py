
import numpy as np
import scipy.interpolate

def quadratic_bspline(x, y, n=100):
    t, c, k = scipy.interpolate.splrep(x, y, k=2)
    spline = scipy.interpolate.BSpline(t, c, k, extrapolate=False)
    
    x_new = np.linspace(x[0], x[-1], n)
    y_new = spline(x_new)
    
    return x_new, y_new

# Example usage
x = np.array([0, 1, 2, 3, 4])
y = np.array([0, 1, 3, 2, 0])

x_new, y_new = quadratic_bspline(x, y)

print(x_new)
print(y_new)
