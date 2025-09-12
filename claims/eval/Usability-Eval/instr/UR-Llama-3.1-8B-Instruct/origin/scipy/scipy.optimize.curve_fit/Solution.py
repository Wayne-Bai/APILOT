from scipy.optimize import curve_fit
import numpy as np

# Define the function to fit (a sine wave in this case)
def func(x, a, b, c):
    return a * np.sin(b*x + c)

# Generate sample data
x = np.linspace(0, 4*np.pi, 100)
y = func(x, 2, 2, 3) + 0.2 * np.random.randn(100)

# Initial guess for parameters
p0 = [1, 1, 1]

# Perform non-linear least squares fit
popt, pcov = curve_fit(func, x, y, p0=p0)

# Print the fitted parameters
print(f"Fitted parameters: a={popt[0]:.2f}, b={popt[1]:.2f}, c={popt[2]:.2f}")

# Plot the data and the fit
import matplotlib.pyplot as plt

plt.plot(x, y, 'ko', label='Data')
plt.plot(x, func(x, *popt), 'r-', label='Fit')
plt.legend()
plt.show()
