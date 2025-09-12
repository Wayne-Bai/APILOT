import numpy as np
from scipy.optimize import curve_fit

def my_function(x, a, b, c):
    # Define the function to be fitted
    return a * np.exp(-b * x) + c

# Generate synthetic data
np.random.seed(0)
xdata = np.linspace(0, 4, 50)
ydata = my_function(xdata, 2, 0.5, 1) + np.random.normal(0, 0.1, xdata.shape)

# Fit the function to the data
params, covariance = curve_fit(my_function, xdata, ydata, p0=(1, 1, 1))

xfit = np.linspace(0, 4, 50)
yfit = my_function(xfit, *params)

print("Fitted parameters:", params)
