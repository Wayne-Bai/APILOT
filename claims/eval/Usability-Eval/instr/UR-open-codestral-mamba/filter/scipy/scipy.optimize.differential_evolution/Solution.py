from scipy.optimize import minimize

# Example objective function (you need to replace this with your multivariate function)
def objective_function(x):
    return (x[0] - 1)**2 + (x[1] - 2.5)**2

# Initial guess for the parameters (you can change this)
x0 = [0, 0]

# Perform optimization
result = minimize(objective_function, x0)

# Print the optimized parameters and the value of the function at this point
print("Optimized Parameters: ", result.x)
print("Value of the function at optimized parameters: ", result.fun)
