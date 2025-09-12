
import numpy as np
from scipy.optimize import minimize

def objective_function(x):
    # Define the objective function to minimize - for example, sum of squares
    return np.sum(np.square(x))

# Define the constraints for the bounds on the variables
bounds = [(0, 10) for i in range(3)]  # Example bounds from 0 to 10 for each variable

# Initial guess for the variables
x0 = np.array([1, 1, 1])

# Call the minimize function with method='trust-constr' to solve the linear least-squares problem with bounds
result = minimize(objective_function, x0, method='trust-constr', bounds=bounds)

print('Optimal variables:', result.x)
print('Optimal value:', result.fun)
