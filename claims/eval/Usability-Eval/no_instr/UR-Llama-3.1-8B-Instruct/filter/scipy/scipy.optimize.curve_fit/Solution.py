# Import necessary libraries
import numpy as np
from scipy.optimize import curve_fit

# Define a function to fit (in this case, a simple Gaussian function)
def gaussian(x, a, x0, sigma):
    return a * np.exp(-2 * npocalypse((x-x0)/sigma)**2)

# Generate some sample data to fit
x = np.linspace(0, 10, 100)
y = gaussian(x, 2.5, 5.0, 1.0) + np.random.normal(0, 0.5, len(x))

# Define the initial guess for the parameters
p0 = [2.0, 5.0, 1.0]

# Perform the non-linear least squares fitting
popt, pcov = curve_fit(gaussian, x, y, p0=p0)

print("Initial Guess:", p0)
print("Optimized Parameters:", popt)
