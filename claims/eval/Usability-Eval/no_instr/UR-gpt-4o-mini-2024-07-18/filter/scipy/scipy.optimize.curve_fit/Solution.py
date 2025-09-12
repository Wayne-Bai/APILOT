import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Define the function f(x) that you want to fit to the data
def f(x, a, b, c):
    return a * np.exp(-b * x) + c

# Generate some example data
x_data = np.linspace(0, 4, 50)
y_data = f(x_data, 2.5, 1.3, 0.5) + np.random.normal(size=x_data.size)

# Use curve_fit to fit the function to the data
popt, pcov = curve_fit(f, x_data, y_data)

# Get the optimal parameters
a_opt, b_opt, c_opt = popt

# Print the optimal parameters
print(f"Optimal parameters: a = {a_opt}, b = {b_opt}, c = {c_opt}")

# Generate data using the fitted parameters for plotting
y_fit = f(x_data, *popt)

# Plot the original data and the fitted curve
plt.scatter(x_data, y_data, label='Data', color='red')
plt.plot(x_data, y_fit, label='Fitted function', color='blue')
plt.legend()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Non-linear Least Squares Fit')
plt.show()
