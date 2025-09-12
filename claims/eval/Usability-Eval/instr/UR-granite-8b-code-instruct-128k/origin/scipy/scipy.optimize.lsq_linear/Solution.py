import scipy.optimize as opt

# Define the objective function
def objective(x):
    return x[0]**2 + x[1]**2

# Define the constraints
constraints = ({'type': 'ineq', 'fun': lambda x: x[0] - 1},
               {'type': 'ineq', 'fun': lambda x: x[1] - 1},
               {'type': 'ineq', 'fun': lambda x: -x[0] - x[1] + 1})

# Set the initial guess
x0 = [0, 0]

# Set the bounds
bounds = [(0, None), (0, None)]

# Solve the problem
result = opt.minimize(objective, x0, constraints=constraints, bounds=bounds)

# Print the result
print(result)
