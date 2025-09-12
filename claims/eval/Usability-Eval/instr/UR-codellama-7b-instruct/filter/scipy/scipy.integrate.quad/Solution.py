
import numpy as np
from scipy import integrate

# Define the function to be integrated
def f(x):
    return x**2 + 1

# Set up the integration limits
a = 0
b = 1

# Compute the definite integral using the Simpson's rule
I = integrate.simps(f, a, b)

print("Definite Integral:", I)
