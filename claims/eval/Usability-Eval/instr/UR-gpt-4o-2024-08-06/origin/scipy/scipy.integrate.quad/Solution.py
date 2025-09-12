import scipy.integrate as spi

# Define the function to integrate
def function_to_integrate(x):
    return x**2

# Define the limits of integration
lower_limit = 0
upper_limit = 1

# Compute the definite integral
result, error = spi.quad(function_to_integrate, lower_limit, upper_limit)

print(f"The definite integral of x^2 from {lower_limit} to {upper_limit} is {result}")
