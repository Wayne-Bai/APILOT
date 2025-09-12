import numpy as np
import scipy.optimize as opt

def f(x, a, b):
    return a * np.exp(b * x)

# Sample data points
xdata = np.array([0, 1, 2, 3, 5, 10])
ydata = np.array([4, 5, 3, 2, 9, 8])

# Non-linear least squares fitting
params, params_covariance = opt.curve_fit(f, xdata, ydata)

print("Optimized parameters (a, b):", params)
print("Covariance of parameter estimates:", params_covariance)
