import numpy as np
from scipy.optimize import curve_fit

# Define the function to fit
def func(x, a, b):
    return a * np.exp(-b * x)

# Given data
x_data = np.array([0, 1, 2, 3, 4, 5])
y_data = np.array([2.0, 1.8, 1.3, 0.5, 0.2, 0.1])

# Use curve_fit to fit the function to the data
parameters, covariance = curve_fit(func, x_data, y_data)

# Extracting the parameters
a, b = parameters

print('Fitted parameters:', parameters)
print('Covariance matrix:', covariance)
