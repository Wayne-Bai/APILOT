import scipy.ndimage
import numpy as np

# Let's assume we have a 3x3 array
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

#Applying the maximum filter on the array
max_filter = scipy.ndimage.maximum_filter(arr, size=3, mode='constant')

print("Original Array:")
print(arr)
print("\nMaximum Filter Array:")
print(max_filter)
