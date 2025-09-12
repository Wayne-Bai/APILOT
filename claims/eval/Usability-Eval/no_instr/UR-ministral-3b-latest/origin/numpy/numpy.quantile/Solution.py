import numpy as np

# You need to specify the data array and the q-th quantile you want to compute.
data = np.array([10, 20, 30, 40, 50])
q = 0.8  # quantile you want to compute

# use the `np.percentile` function to compute the q-th quantile
result = np.percentile(data, q * 100, axis=None)

print(result)
