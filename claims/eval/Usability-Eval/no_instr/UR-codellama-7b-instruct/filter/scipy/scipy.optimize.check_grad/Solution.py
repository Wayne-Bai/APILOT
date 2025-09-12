
import numpy as np
from scipy.optimize import approx_fprime

# Define the function and its inputs
def myfunc(x):
  return np.sin(x)

# Define the input values for x
x = np.array([0, 1, 2, 3])

# Compute the gradient of myfunc using approx_fprime
grad = approx_fprime(myfunc, x, h=1e-4)

print("The gradient of myfunc at x=0 is:", grad[0])
print("The gradient of myfunc at x=1 is:", grad[1])
print("The gradient of myfunc at x=2 is:", grad[2])
print("The gradient of myfunc at x=3 is:", grad[3])
