from scipy.optimize import minimize

# Define the function to optimize
def func(x):
    return (x - 2)**2

# Set the initial guess
x0 = 0

# Set the bounds for the variables
bounds = [(None, None)]

# Perform the optimization
result = minimize(func, x0, bounds=bounds, method='SLSQP')

# Print the result
print("Global minimum at:", result.x)
print("Minimum value:", result.fun)
