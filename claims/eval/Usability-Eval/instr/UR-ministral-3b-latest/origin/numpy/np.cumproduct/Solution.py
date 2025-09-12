import numpy as np

# Assuming x is your numpy array
x = np.array([1, 2, 3, 4])

# Return the cumulative product of elements along axis 0 (default)
cumulative_product = np.cumprod(x, axis=0)
print(cumulative_product)
