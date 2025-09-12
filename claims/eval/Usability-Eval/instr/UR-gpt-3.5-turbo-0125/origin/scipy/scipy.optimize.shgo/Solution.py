
import numpy as np
from scipy.optimize import shgo

def test_function(x):
    return x[0]**2 + x[1]**2

bounds = [(-2, 2), (-2, 2)]

result = shgo(test_function, bounds)

global_min = result.fun
arg_min = result.x

print("Global minimum value:", global_min)
print("Achieved at point:", arg_min)
