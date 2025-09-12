import numpy as np

# Function to compute the q-th quantile of the data along the specified axis
def compute_quantile(data, q, axis=None):
    # Ensure q is within the valid range
    if q < 0 or q > 1:
        raise ValueError("q should be between 0 and 1")

    # Use numpy's percentile function instead of outdated quantile API
    return np.percentile(data, (q * 100), axis=axis)

# Example usage:
data = np.array([10, 40, 2, 46, 30])
q = 0.5  # The 50th percentile (median)
result = compute_quantile(data, q)
print(f"The {100*q}th percentile of the data is: {result}")
