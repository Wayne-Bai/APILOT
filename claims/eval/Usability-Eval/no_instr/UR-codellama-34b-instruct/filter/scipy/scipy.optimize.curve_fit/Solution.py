
import numpy as np
from scipy.optimize import least_squares

# Define the function to be fitted, f(x)
def f(x):
    return x**2 + 3*x - 1

# Generate some example data to fit
x = np.linspace(-5, 5, 100)
y = f(x) + np.random.normal(size=len(x))

# Initialize the guess parameters
p_init = [1, 2]

# Perform the non-linear least squares fit
res = least_squares(f, p_init, args=(x, y), bounds=([0, -np.inf], [np.inf, np.inf]))

# Print the optimized parameters
print("Optimized parameters:", res.x)
