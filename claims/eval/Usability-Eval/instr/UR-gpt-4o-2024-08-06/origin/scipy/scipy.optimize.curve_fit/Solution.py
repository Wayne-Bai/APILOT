import numpy as np
from scipy.optimize import least_squares

# Example data
x_data = np.array([1, 2, 3, 4, 5])
y_data = np.array([1.5, 1.7, 3.2, 4.5, 4.9])

# Define the model function to fit to the data
def model_function(x, a, b, c):
    return a * np.exp(-b * x) + c

# Define the residual function for least squares
def residual_function(params, x, y):
    return model_function(x, *params) - y

# Initial guess for the parameters
initial_params = np.array([1.0, 1.0, 1.0])

# Perform the non-linear least squares fitting
result = least_squares(residual_function, initial_params, args=(x_data, y_data))

# Extract the fitted parameters
fitted_params = result.x

print("Fitted Parameters:", fitted_params)

# Optional: Use the fitted parameters to calculate the fitted values
fitted_values = model_function(x_data, *fitted_params)

print("Fitted Values:", fitted_values)
