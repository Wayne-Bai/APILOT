import numpy as np

# Sample array
array = np.array([1, 2, 3, 4])

# Calculating the cumulative product along the default axis
cumulative_product = np.cumprod(array)

print(cumulative_product)
