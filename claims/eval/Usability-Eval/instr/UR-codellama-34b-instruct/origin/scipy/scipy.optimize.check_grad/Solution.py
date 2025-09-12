from scipy.misc import check_grad

def grad(x):
    # Gradient function for a scalar-valued function of one variable
    return x**2

def func(x):
    # Function to compute the finite difference approximation of the gradient
    return (grad(x + 1) - grad(x - 1)) / (2 * h)

h = 0.0001  # Stepsize for finite differences
x = 2.5     # Point at which to evaluate the gradient
analytical_grad = grad(x)
numerical_grad = func(x)
error = check_grad(grad, x, h=h)
print("Maximum absolute error:", error[0])
print("Relative error:", error[1])
