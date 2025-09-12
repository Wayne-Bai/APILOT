from scipy.optimize import minimize_scalar

# Define the multivariate function (example: a simple function f(x, y) = (x - 1)**2 + (y - 2)**2)
def multivariate_function(x):
    return (x[0] - 1)**2 + (x[1] - 2)**2

# Starting point
initial_guess = [0, 0]

# Minimize the function
result = minimize_scalar(multivariate_function, method='SLSQP', bounds=((None, None), (None, None)), options={'x0': initial_guess})

print("Global minimum:", result.x)
