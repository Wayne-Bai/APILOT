import numpy as np

def quantile(data, q, axis=None):
    return np.percentile(data, q, axis=axis)

# Example usage
data = np.array([[10, 7, 4], [3, 2, 1]])
q = 50  # for median
axis = 0  # compute along the column
result = quantile(data, q, axis)
print(result)
