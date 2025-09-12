# Import necessary module
from scipy import integrate

# Define the integrand function (the function to be integrated)
def integrand(x):
    return x**2 + 4*x + 7

# Define the limits of integration (lower limit and upper limit)
a = 0
b = 2

# Perform the definite integral
result, error = integrate.quad(integrand, a, b)

print(f"The definite integral is: {result}")
print(f"The error estimate is: {error}")
