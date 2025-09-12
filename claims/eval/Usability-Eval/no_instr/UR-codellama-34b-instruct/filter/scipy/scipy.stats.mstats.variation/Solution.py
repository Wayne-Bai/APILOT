import numpy as np
from scipy.stats import skewness

# Sample data
data = np.array([1, 2, 3, 4, 5])

# Compute the coefficient of variation
cv = skewness(data)

print("Coefficient of variation:", cv)
