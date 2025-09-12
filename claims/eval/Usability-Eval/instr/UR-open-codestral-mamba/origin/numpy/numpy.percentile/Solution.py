import numpy as np

# Example usage
data = np.array([[10, 7, 4], [3, 2, 1]])
percentile_value = 50  # to get the median
axis = 0

percentile_result = np.percentile(data, percentile_value, axis=axis)
percentile_result
