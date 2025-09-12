import numpy as np
from scipy.stats import variation

# Example data
data = np.array([10, 12, 23, 23, 16, 23, 21, 16])

# Compute the coefficient of variation
cv = variation(data)

print("Coefficient of Variation:", cv)
