import numpy as np
from scipy.optimize import approx_fprime

# Define your function
def func(x):
    return np.sum(x**2)

# Define your gradient function
def grad(x):
    return 2*x

# Create a test point
x0 = np.array([1.0, 2.0, 3.0])

# Get the gradient using approximate_fprime from scipy
approx_grad = approx_fprime(x0, func, epsilon=1e-8)

# Get the gradient using your function
actual_grad = grad(x0)

# Compare the two
np.testing.assert_array_almost_equal(actual_grad, approx_grad, decimal=5,
                                      err_msg='Results are not close enough!')

print("Gradient function is correct.")
