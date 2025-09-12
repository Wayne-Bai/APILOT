import numpy as np
from scipy.optimize import curve_fit

# Define a sample function and data
def f(x, a, b):
    return a*np.sin(b*x)

x = np.linspace(0, 10, 50)
y = f(x, a=2, b=3) + np.random.normal(size=len(x))

# Perform non-linear least squares fit
popt, _ = curve_fit(f, x, y)

# Print the optimized parameters
print(popt)
