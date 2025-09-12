import numpy as np
from scipy.optimize import minimize

def my_func(x):
    return x[0]**2 + x[1]**2

x0 = np.array([1, 2])  # initial guess
res = minimize(my_func, x0, method='nelder-mead')

print(res)
