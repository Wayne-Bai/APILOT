import numpy as np
from scipy.optimize import curve_fit

# Define the function to fit
def f(x, a, b, c):
    """
    Non-linear function to fit the data.
    
    Parameters:
    x (array): Input data
    a (float): Amplitude
    b (float): Offset
    c (float): Exponential decay constant
    
    Returns:
    array: The fitted function values
    """
    return a * np.exp(-b * x) + c

# Generate some noisy data
x_data = np.linspace(0, 4, 50)
y_data = f(x_data, 2.5, 1.3, 0.5) + np.random.normal(0, 0.2, 50)

# Initial guess for the parameters
p0 = [1, 1, 1]

# Bounds for the parameters (optional)
bounds = ([0, 0, 0], [5, 2, 2])

# Perform the fit
popt, pcov = curve_fit(f, x_data, y_data, p0=p0, bounds=bounds)

# Print the fitted parameters
print("Fitted parameters: a = %.2f, b = %.2f, c = %.2f" % tuple(popt))

# Calculate the fitted function values
y_fit = f(x_data, *popt)

# Plot the data and the fitted function
import matplotlib.pyplot as plt

plt.plot(x_data, y_data, 'ko', label="Data")
plt.plot(x_data, y_fit, 'r-', label="Fit")
plt.legend()
plt.show()
