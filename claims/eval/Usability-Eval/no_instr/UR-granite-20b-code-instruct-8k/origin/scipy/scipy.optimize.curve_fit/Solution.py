from scipy.optimize import curve_fit

# Define the function to be fitted
def f(x, a, b, c):
    return a * x**2 + b * x + c

# Define the data to be fitted
x_data = [1, 2, 3, 4, 5]
y_data = [2, 4, 5, 4, 2]

# Perform the non-linear least squares fit
fit_params, fit_covariance = curve_fit(f, x_data, y_data)

# Print the fit parameters
print("Fit parameters:", fit_params)
