import scipy.integrate as spi

# Define the function to integrate
def func(x):
    return x**2

# Compute the definite integral
result, error = spi.quad(func, 0, 1)  # integrating from 0 to 1

print("Integral result:", result)
print("Estimate of error:", error)
