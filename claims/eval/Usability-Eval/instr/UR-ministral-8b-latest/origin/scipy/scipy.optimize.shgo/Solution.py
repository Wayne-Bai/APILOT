import numpy as np
from scipy.optimize import shgo
from scipy.optimize import minimize

def objective_function(x):
    # Example objective function
    return x[0]**2 + x[1]**2

# Bounds for SHGO
bounds = [(-10, 10), (-10, 10)]

# Constraints for SHGO (if any)
# cons = ({'type': 'eq', 'fun': lambda x: x[0] + x[1] - 10}, {'type': 'ineq', 'fun': lambda x: x[0]**2 + x[1]**2 - 25})
cons = ({'type': 'eq', 'fun': lambda x: 0}, {'type': 'ineq', 'fun': lambda x: 0})

# Optimize using SHGO optimization method
result = minimize(objective_function, [0, 0], method='shgo', bounds=bounds, constraints=cons)

print("Optimized result:", result.x)
