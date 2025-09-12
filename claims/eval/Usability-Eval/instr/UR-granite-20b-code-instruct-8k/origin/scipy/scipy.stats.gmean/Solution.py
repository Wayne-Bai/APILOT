
import numpy as np
from scipy.stats.mstats import gmean

# Create example data
data = np.array([[1, 2, 3], [4, 5, 6]])
weights = np.array([0.2, 0.3, 0.5])

# Compute weighted geometric mean
result = gmean(data, axis=0, weights=weights)

print(result)
