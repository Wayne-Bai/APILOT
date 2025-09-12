import scipy.integrate as integrate

# Define the function to integrate
def integrand(x):
    return x**2

# Compute the definite integral from 0 to 1
result, error = integrate.quad(integrand, 0, 1)

print("The result of the integral is:", result)
print("Estimated error:", error)
