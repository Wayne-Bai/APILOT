import scipy.optimize as opt
import numpy as np

def my_function(x):
    return x[0]**2 + 2*x[1]**2 + np.exp(x[0]*x[1])

def gradient(x):
    dx = 2*x[0] + x[1]*np.exp(x[0]*x[1])
    dy = 4*x[1] + x[0]*np.exp(x[0]*x[1])
    return np.array([dx, dy])

x0 = np.array([1.0, 2.0])

# Check the gradient using the scipy.optimize.check_grad function
diff = opt.check_grad(my_function, gradient, x0)
print("Difference between the numerical and analytical gradients:", diff)
