import scipy.integrate as integrate
import numpy as np

# Define the function to integrate
def f(x):
    return np.exp(-x**2)

# Define the limits of integration
a = -1
b = 1

# Compute the definite integral using scipy.integrate.quad
result, error = integrate.quad(f, a, b)

print("The definite integral is: ", result)
print("The error in the integral is: ", error)
