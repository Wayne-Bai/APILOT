from scipy.optimize import shgo

# Example function to find the minimum value
def my_func(x):
    return x**2

# Define the bounds for the SHG optimization
bounds = [(0, 1), (0, 1)]

# Use SHG optimization to find the global minimum
result = shgo(my_func, bounds)

# Print the result
print('The global minimum of the function is:', result.fun)
print('The global minimum occurs at:', result.x)
