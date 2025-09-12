
import numpy as np

# create an array with random values
a = np.random.rand(10)

# print the original array
print("Original array:")
print(a)

# calculate the cumulative product along axis 0 (rows)
cumprod = np.cumprod(a, axis=0)

# print the resulting array
print("\nCumulative product along axis 0:")
print(cumprod)
