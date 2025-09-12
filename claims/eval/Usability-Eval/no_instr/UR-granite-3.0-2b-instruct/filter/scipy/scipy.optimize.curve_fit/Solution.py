from scipy.optimize import leastsq
import numpy as np

# Define the function to fit
def f(x, a, b):
    return a * np.exp(-b * x)

# Generate some data
xdata = np.array([0, 1, 2, 3, 4])
ydata = f(xdata, 1, 0.5) + np.random.normal(size=len(xdata))

# Define the residual function for non-linear least squares
def residuals(p, x, y):
    a, b = p
    return y - f(x, a, b)

# Perform the non-linear least squares fit
p, _ = leastsq(residuals, (1, 0.5), args=(xdata, ydata))

# Print the fitted parameters
print("Fitted parameters:", p)
