import numpy as np

def compute_quantile(data, q, axis=None):
    return np.percentile(data, q*100, axis=axis)

# Example usage
data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
q = 0.5  # Median
result = compute_quantile(data, q)
print(result)
