import numpy as np
from scipy.misc import derivative

def f(x):
    return x**2

def numerical_gradient(f, x):
    h = 1e-6
    return (f(x+h) - f(x))/h

x = 1.0

analytic_gradient = 2*x
numerical_gradient = numerical_gradient(f, x)

print("Analytic Gradient:", analytic_gradient)
print("Numerical Gradient:", numerical_gradient)

if np.abs(analytic_gradient - numerical_gradient) < 1e-6:
    print("Gradient Check Passed!")
else:
    print("Gradient Check Failed!")
