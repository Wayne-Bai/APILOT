
import numpy as np

# Create numpy arrays to be stacked
array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[5, 6], [7, 8]])

# Vertical stacking of arrays
stacked_array = np.vstack((array1, array2))

print("Stacked Array:")
print(stacked_array)
