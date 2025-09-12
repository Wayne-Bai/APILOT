from scipy.optimize import minimize
import numpy as np

# Define the multivariate function
def multivariate_function(x):
    # Replace this with your actual multivariate function
    return np.sum(x**2)

# Define the constraints (if any)
constraints = {'type': 'ineq', 'fun': lambda x: x[0] - 1}

# Initialize the starting point for the optimization
x0 = np.array([0.0, 0.0])

# Perform the optimization
result = minimize(multivariate_function, x0, constraints=constraints)

# Print the result
print("Global minimum found at:", result.x)
print("Minimum value:", result.fun)
