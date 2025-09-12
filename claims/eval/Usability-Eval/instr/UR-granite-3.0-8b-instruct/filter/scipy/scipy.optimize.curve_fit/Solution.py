from scipy.optimize import least_squares
import numpy as np

# Define the function to fit
def f(x, a, b):
    return a * np.exp(b * x)

# Generate some data
xdata = np.array([1, 2, 3, 4, 5])
ydata = np.array([1.2, 2.3, 3.4, 4.5, 5.6])

# Define the residual function
def residuals(params, x, y):
    a, b = params
    return y - f(x, a, b)

# Perform the fit
result = least_squares(residuals, [1, 1], args=(xdata, ydata))

# Print the results
print("Optimal parameters: a =", result.x[0], "b =", result.x[1])
