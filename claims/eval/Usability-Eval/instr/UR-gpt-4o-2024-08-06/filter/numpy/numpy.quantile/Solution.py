import numpy as np

# Sample data
data = np.array([[10, 7, 4], [3, 2, 1]])

# Define the q-th quantile
q = 0.5  # This represents the 50th percentile or median

# Compute the q-th quantile along the specified axis
# Axis can be 0 (column-wise) or 1 (row-wise), or None for the entire array
quantile_result = np.quantile(data, q, axis=0)

print("Quantile along the specified axis:", quantile_result)
