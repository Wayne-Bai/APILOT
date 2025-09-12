import numpy as np
from scipy.stats import wmean

# calculate weighted harmonic mean along axis=0
data = np.array([[1, 2], [3, 4], [5, 6]])
weights = np.array([0.2, 0.3, 0.5])
result = wmean(data, weights=weights, axis=0)
print(result)
