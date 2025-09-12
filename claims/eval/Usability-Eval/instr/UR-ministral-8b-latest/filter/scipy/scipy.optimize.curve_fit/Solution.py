import numpy as np
import scipy.optimize as opt

# Sample data
x_data = np.array([1, 2, 3, 4, 5])
y_data = np.array([1.2, 2.5, 3.1, 4.2, 5.8])

# Define the function to fit
def func(x, a, b, c):
    return a * np.exp(-b * x) + c

# Initial guesses for the parameters a, b, and c
initial_guesses = (1.0, 0.1, 1.0)

# Perform non-linear least squares fit
fit_params, _ = opt.curve_fit(func, x_data, y_data, p0=initial_guesses)

# Extract the fitted parameters
a_fit, b_fit, c_fit = fit_params

# Print the fitted parameters
print(f"Fitted parameters: a = {a_fit:.4f}, b = {b_fit:.4f}, c = {c_fit:.4f}")

# Generate the fit curve
x_fit = np.linspace(min(x_data), max(x_data), 100)
y_fit = func(x_fit, *fit_params)

# Plot the data and the fit curve
import matplotlib.pyplot as plt
plt.scatter(x_data, y_data, label='Data')
plt.plot(x_fit, y_fit, label='Fit')
plt.legend()
plt.show()
