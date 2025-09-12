import numpy as np
from scipy.optimize import curve_fit

# Define the function to fit
def f(x, a, b, c):
    return a * np.exp(-b * x) + c

# Generate some data
xdata = np.linspace(0, 4, 50)
ydata = f(xdata, 2.5, 1.3, 0.5) + 0.2 * np.random.normal(size=len(xdata))

# Fit the function to the data
popt, pcov = curve_fit(f, xdata, ydata, p0=(1, 1, 1))

print("Optimal parameters:", popt)
