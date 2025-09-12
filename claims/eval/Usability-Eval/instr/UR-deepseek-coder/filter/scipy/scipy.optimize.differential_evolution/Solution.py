import numpy as np
from scipy.optimize import minimize

# Define the multivariate function to minimize
def objective_function(x):
    return x[0]**2 + x[1]**2 + x[2]**2

# Initial guess
initial_guess = np.array([1.0, 1.0, 1.0])

# Perform the minimization
result = minimize(objective_function, initial_guess, method='BFGS')

# Print the result
print("Optimal solution:", result.x)
print("Function value at optimal solution:", result.fun)
