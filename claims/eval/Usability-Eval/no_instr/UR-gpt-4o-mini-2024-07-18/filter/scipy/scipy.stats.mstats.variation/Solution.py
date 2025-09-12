import numpy as np
from scipy.stats import variation

# Sample data
data = np.array([10, 20, 30, 40, 50])

# Compute the coefficient of variation
cv = variation(data)

print("Coefficient of Variation:", cv)
