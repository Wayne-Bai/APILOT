import scipy.optimize as opt
import numpy as np

# Define the function we are trying to fit
def f(x, a, b):
    return a * np.exp(-b * x)

# Generate some noisy data
x_data = np.linspace(0, 4, 50)
y_data = f(x_data, 2.5, 1.3) + np.random.normal(size=50)

# Define our error function
def err(params):
    a, b = params
    return f(x_data, a, b) - y_data

# Use non-linear least squares to fit our function to the data
params = opt.least_squares(err, [1.0, 1.0]).x

# Print the fitted parameters
print(f"Fitted parameters: a = {params[0]} and b = {params[1]}")
