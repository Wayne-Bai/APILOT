
from scipy.optimize import shgo
import numpy as np
# Define the function to be minimized
def f(x):
    return x[0]**2 + x[1]**2
# Define the bounds for the variables
bounds = [(0, np.inf), (0, np.inf)]
# Perform the SHG optimization
result = shgo(f, bounds)
# Print the result
print(result)
