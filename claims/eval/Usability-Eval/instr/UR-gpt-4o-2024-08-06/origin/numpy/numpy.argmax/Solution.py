import numpy as np

# Sample numpy array
array = np.array([[3, 6, 1],
                  [8, 5, 2],
                  [7, 4, 9]])

# Returns the indices of the maximum values along the specified axis
max_indices_axis_0 = np.argmax(array, axis=0)  # Along columns
max_indices_axis_1 = np.argmax(array, axis=1)  # Along rows

print("Indices of max values along columns:", max_indices_axis_0)
print("Indices of max values along rows:", max_indices_axis_1)
