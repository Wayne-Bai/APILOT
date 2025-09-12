import numpy as np
from scipy.optimize import minimize

# Define the multivariate function
def objective_function(x):
    return x[0]**2 + x[1]**2 + x[0]*x[1] + x[0] + x[1]

# Initial guess for the variables
initial_guess = np.array([0, 0])

# Call the minimize function from scipy.optimize
result = minimize(objective_function, initial_guess, method='BFGS')

# Output the results
print("Global minimum value:", result.fun)
print("Global minimum location:", result.x)
