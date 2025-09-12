
import numpy as np
from scipy.optimize import minimize

# Define the objective function and constraints
def objective_function(x):
    return (x[0] - 1)**2 + (x[1] - 2)**2  # Example objective function

def constraint(x):
    return x[0] + x[1] - 3

# Define bounds for the variables
bound_x0 = (0, 5)  # Lower and upper bounds for x[0]
bound_x1 = (0, 5)  # Lower and upper bounds for x[1]
bounds = [bound_x0, bound_x1]

# Initial guess
x0 = np.array([0, 0])

# Solve the linear least-squares problem with bounds
result = minimize(objective_function, x0, bounds=bounds, constraints={'fun': constraint, 'type': 'eq'})

# Print the result
print("Optimal solution:")
print(result.x)
