import numpy as np
from scipy.optimize import minimize

# Define the function to minimize
def objective(x):
    """
    Objective function to minimize.
    
    Parameters:
    x (numpy array): Vector of input parameters.
    
    Returns:
    float: The value of the objective function at the given x.
    """
    return (x[0] - 1) ** 2 + 100 * (x[1] - x[0] ** 2) ** 2

# Initial guess
x0 = np.array([-1.2, 1])

# Bounding box constraints
bounds = [(-3, 3), (-3, 3)]

# Constraints
cons = ({'type': 'ineq', 'fun': lambda x:  x[0] + x[1] - 2},
        {'type': 'ineq', 'fun': lambda x:  2 - x[0] + x[1]})

# Run the minimizer
res = minimize(objective, x0, method='SLSQP', bounds=bounds, constraints=cons)

# Print the result
print("Minimum value: ", res.fun)
print("Optimal parameters: ", res.x)

# To get the global minimum separately, you might be required to try different initial guess. 
# Therefore, consider creating a function around minimize to try extra initial guesses.
