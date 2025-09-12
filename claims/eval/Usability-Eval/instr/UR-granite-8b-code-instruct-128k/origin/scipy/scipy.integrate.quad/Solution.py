import scipy.integrate as spi

# Define the function to integrate
def f(x):
    return x**2

# Define the integration limits
a = 0
b = 1

# Compute the integral
integral, error = spi.quad(f, a, b)

# Print the result
print("The integral of f(x) from 0 to 1 is:", integral)
