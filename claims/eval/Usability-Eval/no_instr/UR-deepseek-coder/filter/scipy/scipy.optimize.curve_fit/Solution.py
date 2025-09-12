import numpy as np
from scipy.optimize import least_squares

# Define the function to be fitted
def model_function(params, x):
    a, b, c = params
    return a * np.sin(b * x) + c

# Define the residual function
def residuals(params, x, y):
    return model_function(params, x) - y

# Example data
x_data = np.array([1, 2, 3, 4, 5])
y_data = np.array([3, 5, 7, 9, 11])

# Initial guess for the parameters
initial_guess = [1, 1, 1]

# Perform the non-linear least squares fit
result = least_squares(residuals, initial_guess, args=(x_data, y_data))

# Extract the fitted parameters
fitted_params = result.x

# Print the fitted parameters
print("Fitted parameters:", fitted_params)

# Evaluate the fitted model on the data points
fitted_y = model_function(fitted_params, x_data)

# Print the fitted values
print("Fitted values:", fitted_y)
