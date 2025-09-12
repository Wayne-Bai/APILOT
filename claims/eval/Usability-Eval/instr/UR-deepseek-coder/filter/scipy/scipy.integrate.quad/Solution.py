import scipy.integrate as integrate

def definite_integral(func, a, b):
    result, _ = integrate.quad(func, a, b)
    return result

# Example usage:
# Define the function to integrate
def my_function(x):
    return x**2

# Compute the definite integral from 0 to 1
integral_result = definite_integral(my_function, 0, 1)
print(integral_result)
