from scipy.optimize import differential_evolution

# Define the objective function
def objective_function(x):
    return x[0] ** 2 + x[1] ** 2

# Define the bounds for the variables
bounds = [(0, 10), (0, 10)]

# Run the differential evolution algorithm
result = differential_evolution(objective_function, bounds)

# Print the result
print("Global minimum at x = {} with a value of {}".format(result.x, result.fun))
