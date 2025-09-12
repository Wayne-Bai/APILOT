
import numpy as np
from scipy.integrate import simps

# Define the function y(x)
def y(x):
    return x**2

# Generate sample data
x = np.linspace(0, 10, 100)
y_values = y(x)

# Integrate y(x) using composite Simpson's rule
integral = simps(y_values, x)

print("Integral using composite Simpson's rule:", integral)
