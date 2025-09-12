# Import necessary libraries
import numpy as np
from scipy.optimize import shgo
import matplotlib.pyplot as plt

# Define the objective function
def objective(x):
    """
    Objective function to minimize.
    
    Parameters:
    x (list): List of variables.
    
    Returns:
    float: Value of the function.
    """
    return x[0]**2 + x[1]**2

# Define the bounds for the variables
bounds = [(-1, 1), (-1, 1)]

# Minimize the function using SHG optimization
res = shgo(objective, bounds, n=200, iters=5, callback=None)

# Print the results
print("Minimum value: ", res.fun)
print("Location of the minimum: ", res.x)

# Plot the function
x1 = np.linspace(bounds[0][0], bounds[0][1], 100)
x2 = np.linspace(bounds[1][0], bounds[1][1], 100)
X, Y = np.meshgrid(x1, x2)
Z = X**2 + Y**2

plt.contourf(X, Y, Z, 50)
plt.colorbar()
plt.scatter(res.x[0], res.x[1], color='red')
plt.show()
