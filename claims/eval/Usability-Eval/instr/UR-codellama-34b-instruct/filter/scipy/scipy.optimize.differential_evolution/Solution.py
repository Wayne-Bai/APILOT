import numpy as np
from scipy.optimize import minimize

# Define the objective function and constraints
def obj_func(x):
    # Your objective function here
    return x**2 + 5*x + 10

cons = {'type': 'ineq', 'fun': lambda x: np.array([-1, -1]), 'args': (None,)}

# Define the initial guess
x_init = np.array([0, 0])

# Optimize using scipy's minimize function
res = minimize(obj_func, x_init, method='SLSQP', constraints=cons)

print('Optimal solution:')
print(res.x)
