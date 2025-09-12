import numpy as np

def compute_percentile(data, q, axis=None):
    return np.percentile(data, q, axis=axis)

# Example usage:
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
q = 50  # 50th percentile (median)
result = compute_percentile(data, q, axis=0)
print(result)
