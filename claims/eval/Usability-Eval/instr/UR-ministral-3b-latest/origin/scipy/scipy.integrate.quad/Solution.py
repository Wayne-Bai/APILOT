from scipy import integrate

# Define the function to integrate
def f(x):
    return x**2 + 2*x + 3

# Set the limits of the integral
a = -3
b = 3

# Compute the definite integral using quad
result, error = integrate.quad(f, a, b)

result, error
