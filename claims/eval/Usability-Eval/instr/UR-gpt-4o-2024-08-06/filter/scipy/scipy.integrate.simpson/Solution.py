import numpy as np
from scipy.integrate import simpson

# Example data
y = np.array([1, 2, 3, 4, 5])  # Sampled data points for y
x = np.array([0, 1, 2, 3, 4])  # Corresponding x values

# Compute the integral
result = simpson(y, x)

print("Integrated value:", result)
