import numpy as np
from scipy.optimize import minimize

# Define the problem data
m = 10
n = 5
A = np.random.rand(m, n)
b = np.random.rand(m)
x_bounds = (np.zeros((n, 2)), np.ones((n, 2)))

# Define the objective function
def obj_fun(x):
    return np.linalg.norm(A @ x - b)

# Solve the problem using SLSQP
res = minimize(obj_fun, x0=np.zeros(n), bounds=x_bounds, method='SLSQP')

# Print the results
print("Optimal solution:", res.x)
print("Objective value:", res.fun)
