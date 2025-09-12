from scipy import integrate

# Define the function
def f(x):
    return x**2

# Define the limits of integration
a, b = 0, 1

# Compute the definite integral
result, error = integrate.quad(f, a, b)

print("The definite integral is: ", result)
