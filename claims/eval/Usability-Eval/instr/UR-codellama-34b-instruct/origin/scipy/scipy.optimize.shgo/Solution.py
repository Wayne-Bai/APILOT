import numpy as np
from scipy.optimize import minimize

def objective_function(x):
    # Define your objective function here
    return np.sum(x**2)

# Initialize the optimization problem
n = 10
x0 = np.zeros(n)
bounds = [(0, 10)] * n
method = 'SHG'

# Run the optimization
result = minimize(objective_function, x0, method=method, bounds=bounds)

# Print the results
print('Optimal solution:', result.x)
print('Minimum value of objective function:', result.fun)
