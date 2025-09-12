
from scipy.stats import variation
import numpy as np

# Generate some sample data
data = np.random.normal(loc=0, scale=1, size=(100,))

# Compute the coefficient of variation using the `variation` function
cv = variation(data)

print("Coefficient of Variation:", cv)
