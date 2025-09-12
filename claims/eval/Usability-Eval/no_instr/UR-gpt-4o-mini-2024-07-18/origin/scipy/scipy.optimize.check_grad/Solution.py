import numpy as np
import scipy.optimize as opt

def function_to_optimize(x):
    return x[0]**2 + x[1]**2

def analytical_gradient(x):
    return np.array([2*x[0], 2*x[1]])

def finite_difference_gradient(func, x, epsilon=1e-8):
    grad = np.zeros_like(x)
    for i in range(len(x)):
        x1 = np.copy(x)
        x2 = np.copy(x)
        x1[i] += epsilon
        x2[i] -= epsilon
        grad[i] = (func(x1) - func(x2)) / (2 * epsilon)
    return grad

# Example point
x0 = np.array([1.0, 2.0])

# Compute gradients
analytical_grad = analytical_gradient(x0)
finite_diff_grad = finite_difference_gradient(function_to_optimize, x0)

# Print results
print("Analytical Gradient:", analytical_grad)
print("Finite Difference Gradient:", finite_diff_grad)

# Check correctness (by computing the difference)
difference = np.linalg.norm(analytical_grad - finite_diff_grad)
print("Difference between gradients:", difference)
