import numpy as np
from scipy.optimize import minimize

def objective_function(x):
    # Example: A simple quadratic function in two variables
    return (x[0] - 1)**2 + (x[1] - 2)**2

# Initial guess for the variables
initial_guess = np.array([0, 0])

# Perform the minimization using the 'BFGS' method
result = minimize(objective_function, initial_guess, method='BFGS')

print("Optimal solution:", result.x)
print("Function value at optimal solution:", result.fun)
