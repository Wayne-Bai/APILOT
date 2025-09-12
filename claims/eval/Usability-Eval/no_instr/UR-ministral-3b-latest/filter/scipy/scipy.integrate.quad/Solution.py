from scipy.integrate import quad

# Define the function to integrate
def f(x):
    return x**2 + 2*x + 1

# Compute the definite integral from 0 to 1
result, error = quad(f, 0, 1)
print(f"The result of the integral from 0 to 1 is: {result}")
