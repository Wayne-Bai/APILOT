import scipy.integrate as sp_integrate

# Define the function to integrate
def f(x):
    return x**2

# Define the limits of integration
a = 0
b = 1

# Compute the definite integral
integral_result = sp_integrate.quad(f, a, b)[0]
integral_result
