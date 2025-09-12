import numpy as np

# Sample data
data = np.array([1, 2, 3, 4, 5])

# Calculate cumulative product along axis 0 (rows)
cumulative_product = np.cumprod(data, axis=0)

# Print the result
print(cumulative_product)
