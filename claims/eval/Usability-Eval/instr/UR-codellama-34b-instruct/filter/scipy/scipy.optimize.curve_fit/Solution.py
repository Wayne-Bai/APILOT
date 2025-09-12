
import numpy as np
from scipy.optimize import least_squares

# Define the function and its derivatives
def f(x, p):
    return p[0] * x**2 + p[1] * x + p[2]

def df(x, p):
    return 2 * p[0] * x + p[1]

# Define the data and initial guess for the parameters
xdata = np.array([1, 2, 3, 4, 5])
ydata = np.array([2, 3, 2, 5, 6])
p0 = [1, 1, 1]

# Perform the least squares fit
result = least_squares(f, p0, args=(xdata, ydata))

# Print the optimized parameters and their uncertainties
print(result.x)
print(np.sqrt(np.diag(result.covar)))
