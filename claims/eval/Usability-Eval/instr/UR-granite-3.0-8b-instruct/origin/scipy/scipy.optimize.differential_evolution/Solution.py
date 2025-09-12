from scipy.optimize import minimize

def objective_function(x):
    # Define your multivariate function here
    return (x[0]**2 + x[1]**2 + x[2]**2)  # Example: a simple quadratic function

# Define the initial guess
x0 = [1.0, 1.0, 1.0]

# Define the bounds for each variable
bounds = [(None, None)] * len(x0)

# Find the global minimum
result = minimize(objective_function, x0, bounds=bounds)

# Print the result
print("Global minimum: ", result.x)
print("Minimum value: ", result.fun)
