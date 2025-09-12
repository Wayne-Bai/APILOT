import numpy as np

# Example array
array = np.array([[1, 1, 1],
                  [1, 1, 1],
                  [1, 1, 0]])  # Change 0 to 1 to test other case

# Test if all elements are True along axis 0 (columns)
result_along_axis0 = np.all(array, axis=0)

# Test if all elements are True along axis 1 (rows)
result_along_axis1 = np.all(array, axis=1)

print("All elements are True along axis 0 (columns):", result_along_axis0)
print("All elements are True along axis 1 (rows):", result_along_axis1)
