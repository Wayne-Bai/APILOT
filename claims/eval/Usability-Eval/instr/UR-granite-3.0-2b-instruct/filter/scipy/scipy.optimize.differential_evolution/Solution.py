import numpy as np
from scipy.optimize import minimize

# Define the multivariate function
def multivariate_function(x):
    # Replace this with your actual multivariate function
    return np.sum(x**2)

# Define the initial guess for the minimum
x0 = np.zeros(10)  # Replace with your initial guess

# Define the constraints (if any)
# constraints = {'type': 'ineq', 'fun': lambda x: x[0] - 1}  # Replace with your constraints

# Define the options for the optimization
options = {'maxiter': 1000, 'disp': True}

# Perform the optimization
result = minimize(multivariate_function, x0, method='SLSQP', options=options)

# Print the results
print("Global minimum found at:", result.x)
print("Minimum value:", result.fun)
