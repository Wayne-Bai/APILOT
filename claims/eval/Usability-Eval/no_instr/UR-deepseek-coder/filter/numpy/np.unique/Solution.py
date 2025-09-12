import numpy as np

# Example array
arr = np.array([1, 2, 2, 3, 4, 4, 5])

# Finding unique elements
unique_elements, indices, counts = np.unique(arr, return_index=True, return_counts=True)

print("Unique elements:", unique_elements)
print("Indices of first occurrences:", indices)
print("Counts of occurrences:", counts)
