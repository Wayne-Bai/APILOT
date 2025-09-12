from scipy import optimize

# Define the function for which to find the minimum
def func(x):
    return x[0] ** 2 + x[1] ** 2

# Define bounds on the variables, for example, [0, 0] <= x <= [1, 1]
bounds = [(0, 1), (0, 1)]

# Perform the minimization using minimizing method
result = optimize.minimize(func, [0, 0], bounds=bounds, method='SLSQP')

# Print the result
print("Optimal solution:", result.x)
print("Function value at minimum:", result.fun)
