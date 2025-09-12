from scipy.optimize import curve_fit
import numpy as np

# Sample data
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 3, 5, 7, 11])

# Define the function to fit
def func(x, a, b):
    return a * np.sin(b * x)

# Perform the non-linear least squares fit
popt, pcov = curve_fit(func, x, y)

# Print the fitted parameters
print("Fitted parameters: a = {}, b = {}".format(popt[0], popt[1]))
