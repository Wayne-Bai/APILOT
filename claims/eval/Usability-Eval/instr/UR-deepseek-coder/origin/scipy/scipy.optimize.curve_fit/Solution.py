import numpy as np
from scipy.optimize import least_squares

# Define the function to be fitted
def f(params, x):
    a, b, c = params
    return a * np.exp(-b * x) + c

# Define the residual function
def residual(params, x, y):
    return f(params, x) - y

# Example data
x_data = np.array([1, 2, 3, 4, 5])
y_data = np.array([2.5, 3.5, 4.5, 5.5, 6.5])

# Initial guess for the parameters
initial_guess = [1.0, 1.0, 1.0]

# Perform the least squares fit
result = least_squares(residual, initial_guess, args=(x_data, y_data))

# Extract the fitted parameters
fitted_params = result.x

print("Fitted parameters:", fitted_params)
