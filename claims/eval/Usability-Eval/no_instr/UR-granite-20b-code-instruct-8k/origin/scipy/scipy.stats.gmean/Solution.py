from scipy.stats import gmean
import numpy as np

# create sample data
data = np.array([[1, 2, 3], [4, 5, 6]])
weights = np.array([0.2, 0.3, 0.5])

# compute weighted geometric mean
result = gmean(data, axis=1, weights=weights)

print(result)
