import numpy as np
from scipy.integrate import quad

# Define the function to integrate
def f(x):
    return np.sin(x)

# Compute the definite integral using quad
result, error = quad(f, 0, np.pi)
print("The result of the integral is:", result)
print("The estimated error is:", error)
