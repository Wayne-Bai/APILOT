# Import necessary library
import numpy as np
from scipy.optimize import least_squares

# Generate a sample problem
# Measure residual between predicted and actual values
def residual(p, x, y):
    y_pred = p[0] + p[1]*x
    return y - y_pred

# Data (x and y values)
x_data = np.array([1, 2, 3, 4, 5])
y_data = np.array([2, 3, 5, 7, 11])

# Initial guess for the parameters
p0 = np.array([0, 0])  # initial guess for slope and intercept

# Bounds for parameters (optional)
bounds = [(-10, 10), (0, 1)]  # bounds for slope and intercept

# Solve the problem with bounds on the variables
res = least_squares(residual, p0, args=(x_data, y_data), bounds=bounds)

# Get the optimized parameters
best_p = res.x
print("Optimized slope:", best_p[1])
print("Optimized intercept:", best_p[0])
