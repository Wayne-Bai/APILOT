import numpy as np
from scipy.optimize import check_grad

def grad_func(x):
    # Define the gradient function here
    pass

def finite_diff_approx(x):
    # Define the finite-difference approximation here
    pass

x = np.array([1.0, 2.0, 3.0])  # Example input
print(check_grad(grad_func, finite_diff_approx, x))
