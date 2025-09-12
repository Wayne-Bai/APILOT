import numpy as np
from scipy.optimize import minimize

# Define the objective function
def objective_function(x):
    return x[0]**2 + x[1]**2  # Example: simple quadratic function

# Initial guess
initial_guess = np.array([1.0, 1.0])

# Perform SHGo optimization
result = minimize(objective_function, initial_guess, method='SHGO')

# Display the results
print("Global minimum found at:", result.x)
print("Function value at minimum:", result.fun)
