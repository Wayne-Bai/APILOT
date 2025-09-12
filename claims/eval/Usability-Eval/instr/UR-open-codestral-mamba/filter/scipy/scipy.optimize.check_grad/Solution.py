from scipy import optimize
import numpy as np

# Gradient function
def grad_f(x):
    # This is just an example gradient function, replace it with your actual function
    return np.array([2*x[0], 3*x[1]])

# Forward finite-difference approximation of gradient
def grad_f_approx(x, h=1e-5):
    grad = np.zeros(x.shape)
    it = np.nditer(x, flags=['multi_index'], op_flags=['readwrite'])
    while not it.finished:
        ix = it.multi_index
        original_value = x[ix]
        x[ix] = original_value + h
        fxh = optimize.rosen(x)  # Replace with your function
        x[ix] = original_value
        grad[ix] = (fxh - optimize.rosen(x)) / h  # Replace with your function
        it.iternext()
    return grad

# Test the gradients at some point
x = np.array([5, 7])
grad_analytical = grad_f(x)
grad_numerical = grad_f_approx(x)
print("Analytical gradient:", grad_analytical)
print("Numerical gradient:", grad_numerical)
