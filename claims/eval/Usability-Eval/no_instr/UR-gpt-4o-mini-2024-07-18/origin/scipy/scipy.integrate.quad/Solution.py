import scipy.integrate as spi

# Define the function to integrate
def f(x):
    return x**2  # Example function: f(x) = x^2

# Set the limits of integration
a = 0  # Lower limit
b = 1  # Upper limit

# Compute the definite integral
integral, error = spi.quad(f, a, b)

print("Definite integral:", integral)
print("Estimated error:", error)
