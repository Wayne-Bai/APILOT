from scipy import integrate

# Define the function to be integrated
def f(x):
    return x**2 + 1

# Set the limits of integration
a = 0
b = 1

# Compute the definite integral using the Romberg method
result = integrate.romberg(f, a, b)

print("The value of the definite integral is:", result)
