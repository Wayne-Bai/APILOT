import numpy as np
from scipy.optimize import check_grad

# Define the function and its gradient
def function(x):
    return np.sum(x**2)

def gradient(x):
    return 2 * x

# Test the gradient function
x0 = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
epsilon = 1e-8

print(check_grad(function, gradient, x0, epsilon=epsilon))
