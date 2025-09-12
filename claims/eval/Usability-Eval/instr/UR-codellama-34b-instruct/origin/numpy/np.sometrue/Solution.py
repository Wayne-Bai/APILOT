
import numpy as np

# Create a sample array
arr = np.array([[1, 2], [3, 4]])

# Test if any element in the first row is greater than 0
print(np.any(arr > 0, axis=0))
