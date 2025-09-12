# Import necessary modules
from scipy import integrate
import numpy as np

# Define the function for which we want to compute the definite integral
def f(x):
    return x**2 + 2*x + 1

# Define the limits of integration
a = 0
b = 3

# Use the quad function to compute the definite integral
result, error = integrate.quad(f, a, b)

# Print the result
print(f"The definite integral of f(x) = x^2 + 2x + 1 from {a} to {b} is: {result}")
