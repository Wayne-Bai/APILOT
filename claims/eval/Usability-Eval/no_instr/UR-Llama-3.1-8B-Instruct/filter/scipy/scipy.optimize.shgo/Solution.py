import numpy as np
from scipy.optimize import shgo
import matplotlib.pyplot as plt

# Define the objective function
def f(x):
    # You can replace this function with your own
    return (x[0] - 1)**2 + (x[1] - 2)**2

# Define the bounds for the variables
bounds = [[0, 2], [0, 3]]

# Run the SHG optimization
res = shgo(f, bounds, iters=50, n=20)

print(f"Minimum: {res.fun}")
print(f"Position of the minimum: {res.x}")

# Plot the function
x = np.linspace(0, 2, 100)
y = np.linspace(0, 3, 100)
X, Y = np.meshgrid(x, y)
Z = (X - 1)**2 + (Y - 2)**2

plt.contourf(X, Y, Z, 50, cmap='viridis')
plt.colorbar(label='f(x, y)')
plt.title('Contour plot of the function f(x, y)')
plt.show()
