
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

cumulative_product = np.cumprod(arr, axis=1)

print(cumulative_product)
