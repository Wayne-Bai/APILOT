
import numpy as np

# Create two arrays to be stacked horizontally
array1 = np.array([[1, 2, 3],
                    [4, 5, 6]])

array2 = np.array([[7, 8],
                    [9, 10]])

# Check if number of rows in both arrays match for horizontal stacking
if array1.shape[0] == array2.shape[0]:
    stacked_array = np.concatenate((array1, array2), axis=1)
    print(stacked_array)
else:
    print("Number of rows should match for horizontal stacking")
