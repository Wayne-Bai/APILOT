import scipy.optimize
import numpy as np

def non_linear_least_squares(data_x, data_y, initial_guess):
    # Assuming f(x, a, b, c) = a * np.exp(-b * x) + c
    def f(x, a, b, c):
        return a * np.exp(-b * x) + c

    # Perform non-linear least squares fit
    result = scipy.optimize.curve_fit(f, data_x, data_y, p0=initial_guess)

    # Return the fitting parameters
    return result

# Example usage:
data_x = np.array([1, 2, 3, 4, 5])
data_y = np.array([0.62, 1.75, 3.38, 5.62, 9.16])
initial_guess = [1, 1, 2]

fit_params = non_linear_least_squares(data_x, data_y, initial_guess)
print(fit_params)
