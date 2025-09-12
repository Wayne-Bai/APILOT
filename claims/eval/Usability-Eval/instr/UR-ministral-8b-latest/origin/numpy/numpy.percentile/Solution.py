import numpy as np

def compute_percentile(data, q, axis=None):
    return np.percentile(data, q, axis=axis)

# Example usage:
data = np.array([10, 20, 30, 40, 50])
q = 50
result = compute_percentile(data, q)
print(f"The {q}-th percentile of the data is: {result}")
