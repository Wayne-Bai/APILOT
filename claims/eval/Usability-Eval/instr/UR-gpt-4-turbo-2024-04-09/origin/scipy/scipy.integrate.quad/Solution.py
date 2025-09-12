import scipy.integrate as spi

def f(x):
    return x**2  # Function to integrate

# Computing the definite integral of f from 0 to 1
result, error = spi.quad(f, 0, 1)
print("Integral result:", result)
print("Error estimate:", error)
