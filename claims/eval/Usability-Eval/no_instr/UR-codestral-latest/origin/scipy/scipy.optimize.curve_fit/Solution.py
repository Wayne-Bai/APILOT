from scipy.optimize import curve_fit
import numpy as np

# Define the function to fit
def func(x, a, b, c):
    return a * np.exp(-b * x) + c

# Generate some data
x_data = np.linspace(0, 4, 50)
y_data = func(x_data, 2.5, 1.3, 0.5) + 0.2 * np.random.normal(size=50)

# Fit the function to the data
popt, pcov = curve_fit(func, x_data, y_data)

print("Optimized parameters:", popt)
