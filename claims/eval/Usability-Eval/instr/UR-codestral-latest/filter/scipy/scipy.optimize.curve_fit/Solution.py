import numpy as np
from scipy.optimize import curve_fit

# Define the function to be fit (e.g., a Gaussian function)
def func(x, a, b, c):
    return a * np.exp(-(x - b)**2 / (2 * c**2))

# Generate some test data
xdata = np.linspace(0, 4, 50)
y = func(xdata, 2.5, 1.3, 0.5)
np.random.seed(1729)
y_noise = 0.2 * np.random.normal(size=xdata.size)
ydata = y + y_noise

# Perform the curve fit
popt, pcov = curve_fit(func, xdata, ydata)

# Print the optimal parameters
print("Optimal parameters: ", popt)
