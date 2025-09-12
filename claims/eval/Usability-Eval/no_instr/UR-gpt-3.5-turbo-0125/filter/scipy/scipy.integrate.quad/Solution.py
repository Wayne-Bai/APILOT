
from scipy.integrate import quad

# Define the function to be integrated
def integrand(x):
    return x ** 2

# Compute the definite integral
result, error = quad(integrand, 0, 1)

print("The definite integral of x^2 from 0 to 1 is:", result)
