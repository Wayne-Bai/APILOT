from scipy.optimize import minimize

# Define the linear function to minimize
def linear_function(x):
    # Define the A and b matrices from the problem
    A = [[1, 2], [2, 3], [3, 4]]
    b = [3, 6, 9]

    return sum([(a * x[0] + b[i] * x[1])**2 for i, a in enumerate(A)])

# Define the bounds on the variables
bounds = [(0, 10), (-10, 10)]

# Use the minimize function to solve the problem
result = minimize(linear_function, [0, 0], method='L-BFGS-B', bounds=bounds)

result
