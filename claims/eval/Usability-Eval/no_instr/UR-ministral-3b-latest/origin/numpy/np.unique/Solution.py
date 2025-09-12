import numpy as np

# Example
arr = np.array([1, 2, 3, 1, 2, 4, 3, 0, -1])

unique_elements = np.unique(arr, return_unique=True, return_inverse=True)

print("Unique elements:", unique_elements[0])
print("First occurrences index:", unique_elements[1])
print("Indexes of reverse unique elements:", unique_elements[2])
