import numpy as np
from scipy.stats import variation

# Sample data
data = np.array([10, 20, 30, 40, 50])

# Calculate the coefficient of variation
cv = variation(data)

print("Coefficient of Variation:", cv)
