
import numpy as np
from scipy.integrate import quad

# Define the function to be integrated
def f(x):
    return x**2

# Set the limits of integration
a = 0
b = 1

# Compute the definite integral
integral_value, error = quad(f, a, b)

print("Definite integral of f(x) from {} to {} is {:.6f}".format(a, b, integral_value))
