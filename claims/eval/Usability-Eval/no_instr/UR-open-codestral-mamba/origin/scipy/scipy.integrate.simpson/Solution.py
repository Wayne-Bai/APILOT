import scipy.integrate as spi
import numpy as np

def y(x):
    # Define your function y(x) here
    return x**2

# If x is None, spacing of dx is assumed
x = np.linspace(0, 1, 10)  # Change this to your actual x values

# Calculate the integral using composite Simpson's rule
integral, error = spi.simps(y(x), x)

print("The integral of the function y(x) is: ", integral)
