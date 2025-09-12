import scipy.integrate as spi

# Define the function to integrate
def f(x):
    return x**2

# Compute the definite integral from 0 to 2
result, error = spi.quad(f, 0, 2)

print("The definite integral is:", result)
