import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Define the model function to be fitted to the data
def model_function(x, a, b, c):
    return a * np.exp(-b * x) + c

# Generate synthetic data with noise
np.random.seed(0)
x_data = np.linspace(0, 4, 50)
y_data = model_function(x_data, 2.5, 1.3, 0.5)
y_noise = 0.2 * np.random.normal(size=x_data.size)
y_data_noisy = y_data + y_noise

# Fit the model function to the noisy data
initial_guess = [1.0, 1.0, 1.0]  # Initial guess for the parameters
optimal_parameters, covariance_matrix = curve_fit(model_function, x_data, y_data_noisy, p0=initial_guess)

# Extract the optimal parameters
a_opt, b_opt, c_opt = optimal_parameters

# Plot the data and the fitted function
plt.figure(figsize=(8, 6))
plt.scatter(x_data, y_data_noisy, label='Noisy data')
plt.plot(x_data, model_function(x_data, *optimal_parameters), color='red', label='Fitted function')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Non-linear Least Squares Fit')
plt.show()

# Print the optimal parameters
print(f"Optimal parameters: a={a_opt}, b={b_opt}, c={c_opt}")
