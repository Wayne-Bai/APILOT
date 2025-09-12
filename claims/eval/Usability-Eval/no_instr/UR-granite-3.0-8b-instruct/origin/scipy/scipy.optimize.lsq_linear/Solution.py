from scipy.optimize import least_squares

# Define the residual function
def residuals(x):
    return [x[0]**2 + x[1] - 1, x[0] - x[1]**2]

# Define the bounds for the variables
bounds = [(None, None), (None, None)]

# Define the initial guess for the variables
x0 = [1, 1]

# Solve the linear least-squares problem with bounds
result = least_squares(residuals, x0, bounds=bounds)

# Print the solution
print(result.x)
