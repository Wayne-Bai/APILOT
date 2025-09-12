import numpy as np
from scipy.optimize import curve_fit

# Example function to fit
def func(x, a, b, c):
    return a * np.exp(-b * x) + c

# Generating artificial data for demonstration
x = np.linspace(0, 4, 50)
y = func(x, 2.5, 1.3, 0.5) + 0.2 * np.random.normal(size=len(x))

# Performing the curve fitting
popt, pcov = curve_fit(func, x, y)

# popt contains the best fit parameters for a, b, and c
print("Fitted parameters:", popt)
