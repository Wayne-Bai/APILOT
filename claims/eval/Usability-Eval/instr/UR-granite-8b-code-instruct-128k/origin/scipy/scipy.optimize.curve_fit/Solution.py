import numpy as np
from scipy.optimize import curve_fit

# Define the function to fit
def f(x, a, b, c):
    return a * np.exp(-b * x) + c

# Generate some data to fit
x = np.linspace(0, 4, 100)
np.random.seed(42)
y = f(x, 2.5, 1.3, 0.5)
y_noise = np.random.normal(0, 0.1, x.shape)
y_data = y + y_noise

# Fit the function to the data
popt, pcov = curve_fit(f, x, y_data)

# Print the results
print(f'Optimal parameters: a={popt[0]}, b={popt[1]}, c={popt[2]}')
print(f'Covariance matrix: {pcov}')
