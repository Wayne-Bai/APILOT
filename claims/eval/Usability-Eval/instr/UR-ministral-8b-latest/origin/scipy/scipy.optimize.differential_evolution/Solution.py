import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt

# Define the multivariate function to minimize
def rosen(x):
    return np.sum(100.0 * (x[1:] - x[:-1]**2.0) ** 2.0 + (1 - x[:-1])**2.0)

# Initial guess
initial_guess = np.array([0.0, 1.0])

# Minimize the function
result = minimize(rosen, initial_guess, method='Nelder-Mead')

# Output the results
print("Minimum value:", result.fun)
print("Optimal parameters:", result.x)

# Visualize the function
x = np.linspace(-2, 2, 200)
y = rosen(x)
plt.plot(x, y)
plt.scatter([result.x[0]], [rosen(result.x)], color='red')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Rosenbrock Function')
plt.show()
