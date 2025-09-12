import scipy.integrate as spi

def function_to_integrate(x):
    # This is the function that we want to integrate
    return x ** 2

integral_value, error = spi.quad(function_to_integrate, 0, 1)

print(f'The integral is: {integral_value} with an estimated error of: {error}')
