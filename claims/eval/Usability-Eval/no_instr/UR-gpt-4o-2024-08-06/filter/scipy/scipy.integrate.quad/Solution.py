import scipy.integrate as spi

# Define the function to integrate
def f(x):
    return x**2  # Example function: x^2

# Set the integration limits
a = 0  # Lower limit
b = 1  # Upper limit

# Compute the definite integral
result, error = spi.quad(f, a, b)

print(f"Definite integral of x^2 from {a} to {b} is {result}")
