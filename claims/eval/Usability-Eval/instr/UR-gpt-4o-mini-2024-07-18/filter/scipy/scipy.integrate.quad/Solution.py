import numpy as np
from scipy.integrate import quad

# Define the function to be integrated
def integrand(x):
    return np.sin(x)  # Example function

# Define the limits of integration
a = 0  # lower limit
b = np.pi  # upper limit

# Compute the definite integral
result, error = quad(integrand, a, b)

# Print the result
print("The integral result is:", result)
print("Estimated error:", error)
