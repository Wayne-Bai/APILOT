from scipy import stats
import numpy as np

# Define the data array
data = np.array([[1, 2, 3], [4, 5, 6]])

# Compute the weighted geometric mean along axis=0
gmean_0 = stats.gmean(data, axis=0, weights=np.array([1, 2, 3]))

print(gmean_0)
