import numpy as np
from scipy.optimize import minimize

# Define the objective function
def objective(x):
    return x**2 + 3*x + 1

# Define the constraints
constraints = [{'type': 'inequality', 'fun': lambda x: x[0] - 2},
               {'type': 'inequality', 'fun': lambda x: x[1] - 2}]

# Initialize the optimizer
method = "SHG"
options = {"maxiter": 100, "tol": 1e-6}

# Run the optimization
res = minimize(objective, [0, 0], method=method, constraints=constraints, options=options)

# Print the results
print("Minimum:", res.x)
