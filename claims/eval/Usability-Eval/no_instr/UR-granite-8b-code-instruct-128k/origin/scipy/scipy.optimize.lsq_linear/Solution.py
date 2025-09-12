import scipy.optimize as opt

# Define the objective function
def objective(x):
    return x[0]**2 + x[1]**2

# Define the constraint function
def constraint(x):
    return x[0] + x[1] - 1

# Set the initial guess
x0 = [0, 0]

# Set the bounds
bounds = [(0, 1), (0, 1)]

# Solve the optimization problem
result = opt.minimize(objective, x0, constraints={'type': 'eq', 'fun': constraint}, bounds=bounds)

# Print the optimal solution
print(result.x)
