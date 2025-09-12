
import numpy as np

def check_gradient(func, grad, x):
    n = x.size
    eps = np.sqrt(np.finfo(float).eps)
    
    grad_fd = np.zeros_like(x)
    for i in range(n):
        x_plus = x.copy()
        x_plus[i] += eps
        grad_fd[i] = (func(x_plus) - func(x)) / eps
    
    grad_analytic = grad(x)
    
    grad_error = np.linalg.norm(grad_analytic - grad_fd) / np.linalg.norm(grad_analytic + grad_fd)
    
    return grad_error

# Usage example:
def my_function(x):
    return np.sum(x**2)

def my_gradient(x):
    return 2*x

x = np.array([1.0, 2.0, 3.0])
error = check_gradient(my_function, my_gradient, x)
print("Relative error of the gradient:", error)
