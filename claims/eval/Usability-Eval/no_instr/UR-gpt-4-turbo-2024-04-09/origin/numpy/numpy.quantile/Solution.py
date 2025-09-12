import numpy as np

def compute_quantile(data, q, axis=None):
    quantile = np.quantile(data, q, axis=axis)
    return quantile

# Example usage:
data = np.array([[10, 7, 4], [3, 2, 1]])
q = 0.5  # Median
result = compute_quantile(data, q, axis=1)
print("Quantiles:", result)
