
import numpy as np
from scipy.integrate import simps

# Define the function y(x)
def f(x):
    return x**2 + 1

# Generate samples along the given axis (e.g., -5 to 5)
x = np.linspace(-5, 5, 100)
y = f(x)

# Integrate y(x) using Simpson's rule
result = simps(y, x)

print(result)
