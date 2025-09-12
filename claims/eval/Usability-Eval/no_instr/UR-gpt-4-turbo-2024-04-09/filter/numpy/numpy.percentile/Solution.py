import numpy as np

def compute_percentile(data, q, axis=None):
    return np.percentile(data, q, axis=axis)

# Example usage:
data = np.array([[10, 7, 4], [3, 2, 1]])
q = 50
result = compute_percentile(data, q, axis=1)
print("Percentiles along axis 1:", result)
