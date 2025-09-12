import numpy as np

def compute_percentile(data, q, axis=None):
    return np.percentile(data, q, axis=axis)

# Example usage:
data_array = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
q = 50  # Compute the 50th percentile
percentile_value = compute_percentile(data_array, q, axis=0)
print(f"The {q}-th percentile along the specified axis is: {percentile_value}")
