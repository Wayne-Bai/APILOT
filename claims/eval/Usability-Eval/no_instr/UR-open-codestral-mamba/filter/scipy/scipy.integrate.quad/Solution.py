import scipy.integrate as integrate
import numpy as np

# Define the function
def function_to_integrate(x):
    return x**2  # replace with your function

# Get the bounds of the integral
start_limit = 0  # replace with your actual start
end_limit = 2    # replace with your actual end

def integral_func(x):
    return function_to_integrate(x)

# Compute the definite integral
result, error = integrate.quad(integral_func, start_limit, end_limit)

result
