import numpy as np
from scipy.optimize import minimize

# Define the multivariate function
def func(x):
    return (x[0]**2 + x[1]**2 + x[2]**2) / 10

# Define the gradient of the function
def grad(x):
    return np.array([2*x[0]/10, 2*x[1]/10, 2*x[2]/10])

# Define the initial guess
x0 = np.array([-1.0, -1.0, -1.0])

# Minimize the function
result = minimize(func, x0, method='SLSQP', jac=grad)

# Print the result
print("Global minimum at x =", result.x)
print("Minimum value =", result.fun)
