
import numpy as np
from scipy.optimize import least_squares

# Define the function f that you want to fit to the data
def model_function(x, params):
    return params[0] * np.exp(-params[1]*x) + params[2]

# Define the objective function for least squares optimization
def objective_function(params, x, y):
    return model_function(x, params) - y

# Generate some example data
np.random.seed(0)
x_data = np.linspace(0, 10, 100)
true_params = [2.5, 0.3, 0.5]
y_data = model_function(x_data, true_params) + 0.2 * np.random.normal(size=x_data.size)

# Initial guess for the parameters
initial_guess = [1.0, 0.2, 0.3]

# Perform non-linear least squares optimization
result = least_squares(objective_function, initial_guess, args=(x_data, y_data))

# Extract the optimized parameters
optimized_params = result.x

print("Optimized parameters:", optimized_params)
