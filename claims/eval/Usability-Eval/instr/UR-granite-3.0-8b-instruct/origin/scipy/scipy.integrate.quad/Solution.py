import scipy.integrate as spi

# Define the function to integrate
def integrand(x):
    return x**2

# Compute the definite integral from 0 to 1
result, error = spi.quad(integrand, 0, 1)

print(f"The definite integral from 0 to 1 of {integrand(x)} is {result} with an error of {error}")
